#!/usr/bin/env python

"""
Copyright (c) 2006-2024 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.common import Backend
from lib.core.common import Format
from lib.core.common import unArrayizeValue
from lib.core.compat import xrange
from lib.core.data import conf
from lib.core.data import kb
from lib.core.data import logger
from lib.core.enums import DBMS
from lib.core.enums import OS
from lib.core.session import setDbms
from lib.core.settings import SYBASE_ALIASES
from lib.request import inject
from plugins.generic.fingerprint import Fingerprint as GenericFingerprint

class Fingerprint(GenericFingerprint):
    def __init__(self):
        GenericFingerprint.__init__(self, DBMS.SYBASE)

    def getFingerprint(self):
        value = ""
        wsOsFp = Format.getOs("Web服务器", kb.headersFp)

        if wsOsFp:
            value += "%s\n" % wsOsFp

        if kb.data.banner:
            dbmsOsFp = Format.getOs("后端数据库管理系统", kb.bannerFp)

            if dbmsOsFp:
                value += "%s\n" % dbmsOsFp

        value += "后端数据库管理系统: "

        if not conf.extensiveFp:
            value += DBMS.SYBASE
            return value

        actVer = Format.getDbms()
        blank = " " * 15
        value += "活动指纹: %s" % actVer

        if kb.bannerFp:
            banVer = kb.bannerFp.get("dbmsVersion")

            if banVer:
                banVer = Format.getDbms([banVer])
                value += "\n%sbanner解析指纹: %s" % (blank, banVer)

        htmlErrorFp = Format.getErrorParsedDBMSes()

        if htmlErrorFp:
            value += "\n%sHTML错误消息指纹: %s" % (blank, htmlErrorFp)

        return value

    def checkDbms(self):
        if not conf.extensiveFp and Backend.isDbmsWithin(SYBASE_ALIASES):
            setDbms("%s %s" % (DBMS.SYBASE, Backend.getVersion()))

            self.getBanner()

            Backend.setOs(OS.WINDOWS)

            return True

        infoMsg = "正在测试 %s" % DBMS.SYBASE
        logger.info(infoMsg)

        if conf.direct:
            result = True
        else:
            result = inject.checkBooleanExpression("transtate=transtate")

        if result:
            infoMsg = "确认 %s" % DBMS.SYBASE
            logger.info(infoMsg)

            result = inject.checkBooleanExpression("suser_id()=suser_id()")

            if not result:
                warnMsg = "后端数据库管理系统不是 %s" % DBMS.SYBASE
                logger.warning(warnMsg)

                return False

            setDbms(DBMS.SYBASE)

            self.getBanner()

            if not conf.extensiveFp:
                return True

            infoMsg = "正在主动指纹识别 %s" % DBMS.SYBASE
            logger.info(infoMsg)

            result = unArrayizeValue(inject.getValue("SUBSTRING(VERSION,1,1)"))

            if result and result.isdigit():
                Backend.setVersion(str(result))
            else:
                for version in range(12, 16):
                    result = inject.checkBooleanExpression("PATINDEX('%%/%d[./]%%',VERSION)>0" % version)

                    if result:
                        Backend.setVersion(str(version))
                        break

            return True
        else:
            warnMsg = "后端数据库管理系统不是 %s" % DBMS.SYBASE
            logger.warning(warnMsg)

            return False