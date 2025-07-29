class Solution {
    private int ROWS, COLS;
    Set<Pair<Integer,Integer>> path = new HashSet();
    public boolean exist(char[][] board, String word) {

        ROWS =  board.length;
        COLS = board[0].length;

        for(int r=0;r<ROWS;r++){
            for(int c=0;c<COLS;c++){

                if(backtrack(r,c,board,word,0)){
                    return true;
                }
            }
        }
        return false;


        
    }

    public boolean backtrack(int r, int c, char[][] board, String word,int i){

        if(i==word.length()){

            return true;
        }

        if(r<0 || r>=ROWS || c<0 || c>=COLS || path.contains(new Pair<>(r,c)) || board[r][c]  !=word.charAt(i)){

            return false;
        }

        path.add(new Pair<>(r,c));

        boolean res = backtrack(r+1,c,board,word,i+1) ||  backtrack(r-1,c,board,word,i+1) ||  backtrack(r,c+1,board,word,i+1) ||  backtrack(r,c-1,board,word,i+1);

        path.remove(new Pair<>(r,c));

        return res;
    }
}