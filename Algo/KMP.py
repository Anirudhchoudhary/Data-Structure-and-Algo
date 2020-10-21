# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class KMP:

    def __int__(self, txt, pattern):
        self.txt = txt
        self.pattern = pattern

    def KMP_(self):
        N = len(self.txt)
        M = len(self.pattern)
        lps = [0] * M
        lps = self.tempory(lps)
        i = 0
        j = 0
        while i < N:
            if self.pattern[j] == self.txt[i]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1

            if j == M:
                print(str(i-j))

                j = lps[j-1]

    def tempory(self, lps):
        M = len(self.pattern)
        lps[0] = 0
        j = 0
        i = 1
        while i < M:
            if self.pattern[i] == self.pattern[j]:
                lps[i] = j + 1
                j += 1
                i += 1
            else:
                # do something
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps


if __name__ == "__main__":
    txt = "AABAACAADAABAABA"
    pattern = "AABA"
    k = KMP()
    k.txt = txt
    k.pattern = pattern
    k.KMP_()
