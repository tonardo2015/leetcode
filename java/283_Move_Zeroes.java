public class Solution {
    public static void moveZeroes(int[] nums){
        // index for the zero location to fill
        int j = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != 0) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                j++;
            }
        }
    }
    public static void main(String[] args){
        int[] nums = {0, 1, 0, 3, 12};
        moveZeroes(nums);
        for(int num: nums){
            System.out.print(num + " ");
        }
    }
}
