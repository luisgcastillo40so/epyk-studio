#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils


class JsClipboard(JsHtml.JsHtml):

  @property
  def content(self):
    return JsObjects.JsObjects.get("(event.clipboardData || window.clipboardData).getData('text')")

  def store(self, jsData=None):
    """
    Description:
    ------------

    """
    if jsData is None:
      return JsObjects.JsVoid("window['%s'] = (event.clipboardData || window.clipboardData).getData('text')" % self.code)

    JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsVoid("window['%s'] = %s" %(self.code, jsData))

  def clear(self):
    """
    Description:
    ------------
    Clear the data store in the clipboard component (not in memory in the current clipboard)
    """
    return JsObjects.JsVoid("window['%s'] = ''" % self.code)

  @property
  def code(self):
    """
    The default data reference
    :return:
    """
    return "%s_data" % self._src.htmlCode

  @property
  def data(self):
    """
    Get the data store in the clipboard component
    """
    return JsObjects.JsString.JsString.get("window['%s']" % self.code)
