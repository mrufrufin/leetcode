// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut x = Self::getval(l1);
        let mut y = Self::getval(l2);
        let mut rem : i32 = 0;
        let mut v  = Vec::new();
        let mut cinsert = true;
        while cinsert || rem > 0 {
            let cur : i32 = x.0 + y.0 + rem;
            rem = cur / 10;
            let curdigit :i32 = cur % 10;
            v.push(curdigit);
            cinsert = x.1.is_some() || y.1.is_some();
            x = Self::getval(x.1);
            y = Self::getval(y.1);
        };
        let mut cend = None;
        for i in (0..v.len()).rev() {
            let node = ListNode {val: v[i], next: cend};
            cend = Some(Box::new(node));
        };
        
        cend
        
    }
    fn getval(cur: Option<Box<ListNode>>) -> (i32, Option<Box<ListNode>>) {
        match cur {
            Some(node) => (node.val, node.next),
            None => (0, None)
        }
    }
}
