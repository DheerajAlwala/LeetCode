#169. Majority Element
class Solution {
    public int majorityElement(int[] nums) {
        int maxC=nums.length/2;
        
        for (int num : nums) {
            int count = 0;
            for (int elem : nums) {
                if (elem == num) {
                    count += 1;
                }
            }

            if (count > maxC) {
                return num;
            }

        }
        return -1;  
    }
}
