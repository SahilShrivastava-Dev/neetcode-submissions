from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my = defaultdict(int)

        # Step 1: Count frequencies
        for num in nums:
            my[num] += 1

        # Step 2: Create buckets
        bucket = [[] for _ in range(len(nums) + 1)]

        # Step 3: Group by frequency
        for num, freq in my.items():
            bucket[freq].append(num)

        # Step 4: Collect top k elements
        result = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result

        return result