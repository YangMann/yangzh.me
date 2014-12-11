# -*- coding: cp936 -*-
import os

__author__ = 'Yang ZHANG'


class Cookie:
    def __init__(self):
        print "Cookie instance initialized. \n"
        self.__l = []
        self.__l1 = []
        self.__l2 = []
        self.__l3 = []
        self.__ln = 0
        self.__n1 = 0
        self.__n2 = 0
        self.__sign = "。|，|,|！|……|!|：|？|\?|；".decode('gbk')
        self.__words1 = [x.decode('gbk', 'ignore').rstrip() for x in
                         file(os.path.join(os.path.abspath(os.path.dirname(__file__)), "dict", "word2.txt"))]
        self.__words2 = [x.decode('gbk', 'ignore').rstrip() for x in
                         file(os.path.join(os.path.abspath(os.path.dirname(__file__)), "dict", "word3.txt"))]
        self.__words3 = [x.decode('gbk', 'ignore').rstrip() for x in
                         file(os.path.join(os.path.abspath(os.path.dirname(__file__)), "dict", "word4.txt"))]
        self.__words4 = [x.decode('gbk', 'ignore').rstrip() for x in
                         file(os.path.join(os.path.abspath(os.path.dirname(__file__)), "dict", "word5.txt"))]
        self.__words5 = [x.decode('gbk', 'ignore').rstrip() for x in
                         file(os.path.join(os.path.abspath(os.path.dirname(__file__)), "dict", "word6.txt"))]
        self.__words0 = [x.decode('gbk', 'ignore').rstrip() for x in
                         file(os.path.join(os.path.abspath(os.path.dirname(__file__)), "dict", "word1.txt"))]
        self.__words = [self.__words1, self.__words2, self.__words3, self.__words4, self.__words5, self.__words0, []]
        self.__number1 = [x.decode('gbk', 'ignore').rstrip() for x in
                          file(os.path.join(os.path.abspath(os.path.dirname(__file__)), "dict", "num2.txt"))]
        self.__number2 = [x.decode('gbk', 'ignore').rstrip() for x in
                          file(os.path.join(os.path.abspath(os.path.dirname(__file__)), "dict", "num3.txt"))]
        self.__number3 = [x.decode('gbk', 'ignore').rstrip() for x in
                          file(os.path.join(os.path.abspath(os.path.dirname(__file__)), "dict", "num4.txt"))]
        self.__number4 = [x.decode('gbk', 'ignore').rstrip() for x in
                          file(os.path.join(os.path.abspath(os.path.dirname(__file__)), "dict", "num5.txt"))]
        self.__number5 = [x.decode('gbk', 'ignore').rstrip() for x in
                          file(os.path.join(os.path.abspath(os.path.dirname(__file__)), "dict", "num6.txt"))]
        self.__number0 = [x.decode('gbk', 'ignore').rstrip() for x in
                          file(os.path.join(os.path.abspath(os.path.dirname(__file__)), "dict", "num1.txt"))]
        self.__number = [self.__number1, self.__number2, self.__number3, self.__number4, self.__number5, self.__number0,
            []]
        self.__bjx = [x.decode('gbk', 'ignore').rstrip() for x in
                      file(os.path.join(os.path.abspath(os.path.dirname(__file__)), "dict", "bjx.txt"))]

    def __binsearch(self, data, key):
        i, j = -1, len(data)
        while i + 1 != j:
            mid = (i + j) >> 1
            if data[mid] < key:
                i = mid
            else:
                j = mid
        if j == len(data) or data[j] != key:
            return -1
        return j

    def __sentence_seg(self, s, sign):
        templ = []
        h = 0
        for i in range(len(s)):
            if s[i] in sign:
                if s[i - 1:i + 2] == "市，让".decode('gbk'):
                    pass
                else:
                    templ += [s[h:i + 1]]
                    h = i + 1
            if i == len(s) - 1:
                if s[len(s) - 1] not in sign:
                    templ.append(s[h:len(s)])
        return templ

    def __userseg(self, word):
        for h in range(len(word)):
            if h + 7 > len(word):
                m = len(word) - h
            else:
                m = 7
            i = m
            while i in range(1, m + 1):
                if "".join(word[h:i + h]) in self.__words[6]:
                    word[h] = "".join(word[h:i + h])
                    del word[h + 1:i + h]
                    break
                i -= 1
            h += 1
        print "word", word  # TODO: remove this logging
        return word

    def __special(self, s):
        i, k, j, t = 0, 0, 0, 0
        a = "《|<".decode('gbk')
        a1 = "》|>".decode('gbk')
        b = "\"|'|“|‘|（".decode('gbk')
        c = "\"|'|”|’|）".decode('gbk')
        d = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ|.".decode('gbk')
        u = "一二三四五七八九十两".decode('gbk')
        # solve book
        while i in range(len(s) - 1):
            if s[i] in a:
                for h in range(40):
                    if h + i < len(s):
                        if s[h + i] in a1:
                            s[i + 1] = "".join(s[i + 1:h + i])
                            del s[i + 2:h + i]
                            break
                    else:
                        break
            i += 1

        # solve letters and numbers
        while k in range(len(s)):
            if s[k] in d:
                for n in range(len(s) - k):
                    if s[k + n] not in d:
                        s[k] = "".join(s[k:k + n])
                        del s[k + 1:k + n]
                        break
            k += 1

        # solve quotations
        while j in range(len(s) - 1):
            if s[j] in b:
                for h1 in range(7):
                    if h1 + j < len(s):
                        if s[h1 + j] in c:
                            s[j + 1] = "".join(s[j + 1:h1 + j])
                            del s[j + 2:h1 + j]
                            break
                    else:
                        break
            j += 1

        # solve digits
        while t in range(1, len(s)):
            if s[t - 1] in u:
                if len(s[t]) < 3:
                    s[t - 1] = s[t - 1:t + 1]  # TODO: Observe the effect of this
            t += 1

        return s

    def __search_(self, h):
        self.__n2 = 1
        print "self.__words", len(self.__words)
        while h > 0:
            if self.__eliminate_("".join(self.__l[h - 6:h]), self.__words[4], 4):
                print "-=6"
                self.__l2.append("".join(self.__l[h - 6:h]))
                h -= 6
            elif self.__eliminate_("".join(self.__l[h - 5:h]), self.__words[3], 3):
                print "-=5"
                self.__l2.append("".join(self.__l[h - 5:h]))
                h -= 5
            elif self.__eliminate_("".join(self.__l[h - 4:h]), self.__words[2], 2):
                print "-=4"
                self.__l2.append("".join(self.__l[h - 4:h]))
                h -= 4
            elif self.__eliminate_("".join(self.__l[h - 3:h]), self.__words[1], 1):
                print "-=3"
                self.__l2.append("".join(self.__l[h - 3:h]))
                h -= 3
            elif self.__eliminate_("".join(self.__l[h - 2:h]), self.__words[0], 0):
                print "-=2"
                self.__l2.append("".join(self.__l[h - 2:h]))
                h -= 2
            elif self.__eliminate_("".join(self.__l[h - 1:h]), self.__words[5], 5):
                print "-=1"
                self.__l2.append("".join(self.__l[h - 1:h]))
                h -= 1
            else:
                print "-=11"
                self.__l2.append("".join(self.__l[h - 1:h]))
                h -= 1
        return

    def ___eliminate(self, s, word, i):
        a = self.__binsearch(word, s)
        if a != -1:
            self.__n1 *= int(self.__number[i][a])
            return True

    def __eliminate_(self, s, word, i):
        a = self.__binsearch(word, s)
        if a != -1:
            self.__n2 *= int(self.__number[i][a])
            return True

    def ___search(self, j):
        self.__n1 = 1
        while j < self.__ln:  # TODO: make __ln global
            if self.___eliminate("".join(self.__l[j:j + 6]), self.__words[4], 4):
                self.__l1.append("".join(self.__l[j:j + 6]))
                j += 6
            elif self.___eliminate("".join(self.__l[j:j + 5]), self.__words[3], 3):
                self.__l1.append("".join(self.__l[j:j + 5]))
                j += 5
            elif self.___eliminate("".join(self.__l[j:j + 4]), self.__words[2], 2):
                self.__l1.append("".join(self.__l[j:j + 4]))
                j += 4
            elif self.___eliminate("".join(self.__l[j:j + 3]), self.__words[1], 1):
                self.__l1.append("".join(self.__l[j:j + 3]))
                j += 3
            elif self.___eliminate("".join(self.__l[j:j + 2]), self.__words[0], 0):
                self.__l1.append("".join(self.__l[j:j + 2]))
                j += 2
            elif self.___eliminate("".join(self.__l[j:j + 1]), self.__words[5], 5):
                self.__l1.append("".join(self.__l[j:j + 1]))
                j += 1
            else:
                self.__l1.append("".join(self.__l[j:j + 1]))
                j += 1
        return

    def __name(self):
        sg = "。|，|,|！|…|!|《|》|<|>|\"|'|:|：|？|\?|、|\||“|”|‘|’|；|—|（|）|·|\(|\)|　".decode('gbk')
        i = 0
        m = ""
        while i in range(len(self.__l1) - 2):
            if len(self.__l1[i]) == 1 and self.__l1[i] not in sg:
                if self.__l1[i] in self.__bjx:
                    if len(self.__l1[i + 1]) == 1 and (self.__l1[i + 1] not in sg):
                        if len(self.__l1[i + 2]) == 1 and (self.__l1[i + 2] not in "是有能".decode('gbk')) and (
                                    self.__l1[i + 2] not in sg):
                            self.__l1[i] = "".join(self.__l1[i:i + 3])
                            del self.__l1[i + 1:i + 3]
                            i += 1
                            m = "t"
                        else:
                            self.__l1[i] = "".join(self.__l1[i:i + 2])
                            del self.__l1[i + 1:i + 2]
                            i += 1
                            m = "t"
                    else:
                        i += 1
                else:
                    i += 1
            else:
                i += 1
        if m != "t":
            h = len(self.__l1) - 2
            if len(self.__l1[h]) == 1 and self.__l1[h] in self.__bjx:
                if len(self.__l1[h + 1]) == 1 and self.__l1[h + 1] not in sg:
                    self.__l1[h] = "".join(self.__l1[h:h + 2])
                    del self.__l1[h + 1]

    def __name_(self):
        sg = "。|，|,|！|…|!|《|》|<|>|\"|'|:|：|？|\?|、|\||“|”|‘|’|；|—|（|）|·|\(|\)|　".decode('gbk')
        i = 0
        m = ""
        while i in range(len(self.__l2) - 2):
            if len(self.__l2[i]) == 1 and self.__l2[i] not in sg:
                if self.__l2[i] in self.__bjx:
                    if len(self.__l2[i + 1]) == 1 and (self.__l2[i + 1] not in sg):
                        if len(self.__l2[i + 2]) == 1 and (self.__l2[i + 2] not in "是有能".decode('gbk')) and (
                                self.__l2[i + 2] not in sg):
                            self.__l2[i] = "".join(self.__l2[i:i + 3])
                            del self.__l2[i + 1:i + 3]
                            m = "t"
                            i += 1
                        else:
                            self.__l2[i] = "".join(self.__l2[i:i + 2])
                            del self.__l2[i + 1:i + 2]
                            m = "t"
                            i += 1
                    else:
                        i += 1
                else:
                    i += 1
            else:
                i += 1
        if m != "t":
            h = len(self.__l2) - 2
            print "self.__l2", self.__l2
            if len(self.__l2[h]) == 1 and self.__l2[h] in self.__bjx:
                if len(self.__l2[h + 1]) == 1 and self.__l2[h + 1] not in sg:
                    self.__l2[h] = "".join(self.__l2[h:h + 2])
                    del self.__l2[h + 1]

    def slice(self, para):
        s = para
        print s
        for i in range(len(s)):
            self.__l.append(s[i:i + 1])

        self.__ln = len(self.__l)
        self.__l = self.__userseg(self.__l)
        self.___search(0)
        self.__search_(0)
        self.__l2 = self.__l2[::-1]
        self.__l1 = self.__special(self.__l1)
        self.__l2 = self.__special(self.__l2)
        self.__name()
        self.__name_()

        if len(self.__l1) < len(self.__l2):
            out_words = '<strong style="font-size:x-large; color:#AB5A0A">|</strong>'.join(self.__l1) + '<br>'
        elif len(self.__l2) < len(self.__l1):
            out_words = '<strong style="font-size:x-large; color:#AB5A0A">|</strong>'.join(self.__l2) + '<br>'
        else:
            if self.__n1 / self.__n2 > 2:
                out_words = '<strong style="font-size:x-large; color:#AB5A0A">|</strong>'.join(self.__l1) + '<br>'
            else:
                out_words = '<strong style="font-size:x-large; color:#AB5A0A">|</strong>'.join(self.__l2) + '<br>'
        print out_words
        return out_words

