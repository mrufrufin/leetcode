use std::cmp;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut sidx : usize = 0;
        let mut endmax :usize = 0;
        let mut cont : bool = true;
        let n = s.len();
        let v : Vec<char> = s.chars().collect();
        while cont {
          let curmax = Self::non_repeat_sub(&v, &sidx);
          endmax = cmp::max(curmax,endmax);
          cont = (sidx + endmax) < n;
          sidx += 1;
        };
        endmax as i32
    }
    fn non_repeat_sub(v: &Vec<char>, sidx: &usize) -> usize {
        let mut seen = Vec::new();
        let n = v.len();
        let mut i = *sidx;
        while i < n && !seen.contains(&v[i]) {
          seen.push(v[i]);
          i += 1; 
        };
        i - sidx
    }
}
