import string

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        sum_linepix = 0
        line_count = 1
        alphabet_list = list(string.ascii_lowercase)
        table = dict(zip(alphabet_list,widths))

        for i in s:
            sum_linepix += table[i]
            if sum_linepix > 100:
                line_count += 1
                sum_linepix = table[i]
            elif sum_linepix == 100:
                line_count += 1
                sum_linepix = 0
        
        if sum_linepix == 0:
            line_count -= 1
            sum_linepix = 100
        
        return [line_count, sum_linepix]
