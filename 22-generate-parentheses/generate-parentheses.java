class Solution {
    public List<String> generateParenthesis(int n) {

        int open=0;
        int closed=0;
        List<String> result = new ArrayList();

        StringBuilder sb = new StringBuilder();

        backtrackParenthesis(0,0,n,sb,result);
        return result;


        
    }

    public void backtrackParenthesis(int open,int closed, int n,StringBuilder sb, List<String> result){

        if (open==n && closed==n){

            result.add(sb.toString());
            return;



        }


        if(open<n){

            sb.append('(');
            backtrackParenthesis(open+1, closed,n,sb,result);
            sb.deleteCharAt(sb.length() - 1);
        }

        if(closed<open){
            sb.append(')');
            backtrackParenthesis(open, closed+1,n,sb,result);
            sb.deleteCharAt(sb.length() - 1);


        }
    }
}