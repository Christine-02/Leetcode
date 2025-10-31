class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
         int newwindow = 0;
         int maxcount =0;
         int count=0;
        for(int i=0;i<nums.length;i++)
        {
            if (nums[i] == 1)
            {
               count++;
            }
            else if (nums[i] != 1)
            {
                newwindow = i;
                maxcount = Math.max(count,maxcount);
                count=0;
                 
            }
        }

        maxcount = Math.max(count,maxcount);

        return maxcount;
    }

}