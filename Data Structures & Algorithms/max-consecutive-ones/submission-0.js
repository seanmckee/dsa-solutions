class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMaxConsecutiveOnes(nums) {
        let maxCons = 0;
        let currentCons = 0;
        for(let i = 0; i < nums.length; i++){
            if(nums[i] === 1){
                currentCons++;
            }else{
                currentCons = 0;
            }
            if(currentCons > maxCons){
                maxCons = currentCons;
            }
        }
        return maxCons;
    }
}
