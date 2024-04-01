class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(num):
            l = 0
            dig_max = 0
            while num:
                val = num%10
                dig_max = max(val, dig_max)
                num //= 10
                l += 1
            return int(str(dig_max)*l)
        ret = 0
        for num in nums:
            val = encrypt(num)
            ret += val
        return ret

