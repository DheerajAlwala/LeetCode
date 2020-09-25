#202. Happy Number
import java.util.HashSet;

class Solution {
    
    private HashSet <Integer> ok = new HashSet <Integer>();
    
    public boolean isHappy(int n) {
        
        if (n == 1) {
            return true;
        }
        
        int sum = 0;
        while (n > 0) {
            sum += (n%10) * (n%10);
            n /= 10;
        }
        
        if (ok.contains(sum)) {
            return false;
        } else {
            ok.add(sum);
        }
        
        return isHappy(sum);
    }
}
