class Solution {
    public int getSum(int a, int b) {
        
        while (b != 0){
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;

    }

    public static void main (String [] args){
        Solution solution = new Solution();

       System.out.println(solution.getSum(1, 2));
        System.out.println(solution.getSum(2, 3));
        System.out.println(solution.getSum(-2, 3));
        System.out.println(solution.getSum(-1, -1));
        
        //bitwise XOR
        //bitwise AND
    }
}
