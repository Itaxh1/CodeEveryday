#https://leetcode.com/problems/contains-duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        hashmap = set()

        for n in nums:
            if n in hashmap:
                return True
            hashmap.add(n)

        return False
        