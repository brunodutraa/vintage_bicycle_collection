const texto = document.getElementsByClassName('text-reduce');
const LIMIT = 200;

for(let t of texto){
    const aboveLimit = t.innerText.length > LIMIT;
    const dotOrEmpty = aboveLimit ? '...' : '';
    t.innerText = t.innerText.substring(0, LIMIT) + dotOrEmpty;
}
