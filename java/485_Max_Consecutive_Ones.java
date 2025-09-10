public class MaxConsecutiveOnes{
    public static int findMaxConsecutiveOnes(int[] nums){
        int maxConsecutive = 0;
        int curCounter = 0;

        for(int num: nums){
            if(num == 1){
                curCounter++;
                maxConsecutive = Math.max(maxConsecutive, curCounter);
            }
            else{
                curCounter = 0;
            }
        }
        return maxConsecutive;
    }
    
    public static void main(String[] args){
        int[] nums = {1, 1, 0, 1, 1, 1};
        System.out.println(findMaxConsecutiveOnes(nums));
    }
}
