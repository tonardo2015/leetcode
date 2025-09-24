public class Solution{
    public int removeDuplicates(int[] nums){
        if(nums.length == 0){
            return 0;
        }
        int uniqNum = 1;
        for(int i = 1; i < nums.length; i++){
            if(nums[i] != nums[i-1]){
                nums[uniqNum] = nums[i];
                uniqNum++;
            }
        }
        return uniqNum;
    }

    public static void main(String[] args){
        int[] nums = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        Solution sol = new Solution();
        System.out.println(sol.removeDuplicates(nums));
    }
}
