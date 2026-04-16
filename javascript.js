
// function firstUnique(str){
//     const count = {}
//     for (const char of str){
//         count[char] = (count[char] || 0) +1;
//     };

//     for (const char of str){
//         if (count[char]===1){
//             return console.log(char);
//         }
//     }
// return console.log(null)
// }
// firstUnique("aabbcc")

for (let i = 1; i<=10; i++){
    let row = "";
    for(let j = 1; j<=i; j++){
        row += "*";
    }
    console.log(row);
    
}

for (let i = 9; i >=1 ; i--){
  console.log("*".repeat(i));
  
    
}


const n = 5
for(let i = 1; i <=n;i++){
    const space = " ".repeat(n-i);
    const starts = "*".repeat( 2 * i - 1);
    console.log(space + starts);
    
}

//reverse the str
let str = "hello";
let reverse ='';
console.log(str[0])
for(let i=str.length -1;i>=0;i--){
    reverse +=str[i]

}
console.log(reverse)