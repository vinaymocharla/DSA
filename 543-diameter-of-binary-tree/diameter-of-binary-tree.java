/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    int maximum = 0;
    public int diameterOfBinaryTree(TreeNode root) {


        height(root);

        return maximum;

       



        
        
    }

    private int height(TreeNode root){

        if(root == null){
            return 0;
        }

        int left = height(root.left);
        int right = height(root.right);

        maximum = Math.max(maximum,left+right);

        return 1+Math.max(left,right);
    }
}