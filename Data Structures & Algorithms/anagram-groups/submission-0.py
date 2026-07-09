class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sortedDict[sorted(num)] = sortedDict[sorted(num)].append(num)
        sortedDict = defaultdict(list)
        for str in strs:
            key = tuple(sorted(str))
            sortedDict[key].append(str)
        return list(sortedDict.values())
        
