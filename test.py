# -*- coding: utf-8 -*-
import unittest
import win2uni


class TestUNI2WIN(unittest.TestCase):

    def test_consonent(self):
        win = '''uc*CipqZ#X!Pwx'"yzAbr,vo[Vt¹@'''
        unicode = '''ကခဂဃငစဆဇဋဌဍဏတထဒဓပဖဗဘမယလသဟဠအဍ္ဎ႑'''
        result = uni2win.convert(win)
        self.assertEqual(unicode, result, "Failed converting Consonent")

    def test_article_one(self):
        win = '''aps;'''
        unicode = '''ဈေး'''
        result = uni2win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article One")

    def test_myanmar_pangram(self):
        win = u'''oD[dkVfrS ÓPfBuD;&Sifonf tm,k၀¹eaq;nGSef;pmudk ZvGefaps;ab;Am'Hyifxuf '''
        unicode = u'''သီဟိုဠ်မှ ဉာဏ်ကြီးရှင်သည် အာယုဝဍ္ဎနဆေးညွှန်းစာကို ဇလွန်ဈေးဘေးဗာဒံပင်ထက် '''
        result = uni2win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Myanmar Pangram")


if __name__ == "__main__":
    unittest.main()
