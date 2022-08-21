// document.write("Hello world!");
// console.log("hello world!");
// console.info("hello world!");
// console.error("hello world!");
// console.warn("Hello world!");

// Урок 2

// var num;
// num = 5;
// const num = 5;
// // num = 7;
// console.log("Переменная:" + num);
// var number;
// number = "Words";
// var num_1=5;
// var num_2="5";

// Урок 3

// var num_1 = 5;
// var num_2 = 15;
// console.log("Результат:"+ (num_1-num_2));

// var num_3 = 5;
// num_3+=1;
// console.log("Результат:"+ (num_1-num_2));

// var str_1 = Number("12");
// var str_2 = Number("2");
// console.log("Результат:"+ (str_1-str_2));

// console.log("Math" + Math.PI);
// console.log("Math" + Math.E);
// console.log("Math" + Math.min(4,4,4,4,1));

// Урок 4

// var number = 15;
// var isHasHouse = true;

// if(number == 5 && isHasHouse == true){
//     console.log("ok");
// } else if(number == 7) {
//     console.log("7");
// } else{
//     console.log("Error");
// }

// var stroka = "word";

// switch(stroka){
//     case "4":
//         console.log("Переменная со значением 4");
//         break;
//     case "45":
//         console.log("Переменная со значением 45");
//         break;
//     case "word":
//         console.log("Переменная со значением word");
//         break;
//     default:
//         console.log("Default");
//         break;
// }

// Урок 5

// var arr = [5,true,"stroka"];
// console.log(arr[0],arr.length);

// var matrix = [
//     [123],
//     [456],
//     [789]
// ];

// matrix[1][0] = 90;

// console.log(matrix);

// Урок 6

// for(var i =0;i<10;i++){
//     console.log(i);
// }

// var j=1000;
// while(j>100){
//     console.log(j);
//     j-=100;
// }

// var x = 100;
// do {
//     console.log(x);
//     x++;
// } while (x<50);

// Урок 7

// for(var i=10;i<=20;i++){
//     if (i % 2 == 0)
//         continue;
//     console.log(i);
// }

// Урок 8

// for(var i=0;i<arr.length;i++);{
//     arr[i]*=2;
//     console.log("Элемент"+(i+1)+":"+arr[i]);
// }

// Урок 9

// alert("Какая хорошая погода"); // всплывающее окно

// var data=confirm("Вы сейчас дома?"); // Вопросительное окно
// if (data){
//     alert("Вы молодец!")
// }

// var data=prompt("Скажите сколько вам лет?");
// console.log(data);
// var var1 =null;

// var person = null;
// if(confirm("Вы точно уверены?")){
//     person = prompt ("Введите ваше имя");
//     alert("Привет,"+person);
// } else {
//     alert("Вы нажали на Отмена");
// }

// Урок 10

// function info(word){
//     console.log(word+"!");
// }
// function summa(a,b){
//     var res = a+b;
//     info(res);
// }
// summa(5,7);

// function summa(arr) {
//     var sum = 0;
//     for(var i=0;i<arr.length;i++)
//         sum+=arr[i];
//     return sum;
// }

// var array =[6,8,1];
// var array_2=[8,8,1,7];
// var array_3=[4,42,53,5];
// var res=summa(array);
// console.log(res);


// var num = 10;
// function info(){
//     var num = 10;
//     console.log(num);
// }
// info();
// console.log(num);

// Урок 11

// var counter = 0;

// function onClickButton(el){
//     counter++;
//     el.innerHTML = "Вы нажали на кнопку:" + counter;

//     console.log(el.value);
//     el.style.background ="red";
//     el.style.color ="blue";
//     el.style.cssText = "border-radius: 5px; border: 0; font-size: 20px";
// }
// function onInput(el){
//     if (el.value == "Hello")
//         alert("И тебе привет!");
//     console.log(el.value);
// }

// Урок 12

// var text = document.getElementById('text');
// text.title = "New text";
// console.log(text.title);
// text.style.color = "red";
// text.style.backgroundColor = "blue";
// text.innerHTML = "New<br>string";
// // document.getElementById('text').style.color = "white";
// // var spans = document.getElementsByTagName('span');
// var spans = document.getElementsByClassName('simple-text');
// for(var i=0; i<spans.length;i++){
//     console.log(spans[i].innerHTML);
// }


// document.getElementById('main-form').addEventListener("submit",checkForm);
// function checkForm(event){
//     event.preventDefault();
//     var el = document.getElementById('main-form');
//     var name = el.name.value;
//     var pass = el.pass.value;
//     var repass = el.repass.value;
//     var state = el.state.value;
//     if (name == "" || pass == "" || state == "")
//         fail = "Заполните все поля";
//     else if(name.length<=1 || name.length >50)
//         fail = "Введите корректное имя";
//     else if(pass != repass)
//         fail = "Пароли должны совпадать";
//     else if(pass.split("&").length > 1)
//         fail = "Некорректный пароль";
//     if(fail !=""){
//         document.getElementById('error').innerHTML = fail;
//         return false;
//     } else{
//         alert("Все данные корректно заполнены");
//         window.location = 'https://itproger.com';
//     }
// }

// Урок 13

// var counter = 0;
// var id=setInterval(my_func,1000);
// function my_func(){
//     counter++;
//     console.log("Counter:" + counter);
//     if(counter==5){
//         clearInterval(id);
//     }
// }

// setInterval(function(){
//     counter++;
//     console.log("Прошло секунд:" + counter);
// },1000);

// Таймер срабатывания кода через время
// setTimeout(my_func, 2000);
// function my_func(){
//     console.log("Timer is warning!");
// }

// Урок 14

//  var date = new Date();
//  console.log(date.getFullYear());
// console.log(date.getMonth()+1);
// console.log("Время:"+ date.getHours()+":"+date.getMinutes());

// var arr = [1,2123,3,4,123215];
// console.log(arr.join(", "))
// console.log(arr.sort());
// var stroka = arr.reverse().join(", ");
// console.log(stroka.split(","));

// class Person{
//     constructor(name,age,happiness){
//         this.name = name;
//         this.age = age;
//         this.happiness = happiness;
//     }
//     info() {
//         console.log("Человек: "+ this.name + ". Возраст:" + this.age);
//     }
// }
// var alex = new Person('Alex',45,true);
// var bob = new Person('Bob',25,false);
// alex.name='alex2';
// alex.info();
// bob.info();

console.log("hello world!");

document.addEventListener('DOMContentLoaded', function(event) {
  fetch('test.csv')
    .then(function(response) {
      if (response.ok) {
        return response.text();
      }
      throw new Error('Не удалось загрузить файл.');
    }).then(function(text) {
      renderTable(text);
    })
    .catch(function(error) {
      console.error('Произошла ошибка при попытке отобразить файл: ' + error.message);
    });
});


// Элемент для выбора файлов.
const INPUT = document.querySelector('input[name="readable"]');
// Элемент для вывода сгенерированной таблицы.
const PREVIEW = document.querySelector('#preview');
// Регулярное выражение для проверки расширения файла.
const REGEX = new RegExp('(.*?)\.(csv)$', 'i');

// Функция, отрабатывающая при выборе файла.
function handleFile(event) {
  // Выбираем первый файл из списка файлов.
  const file = event.target.files[0];

  // Если файл выбран и его расширение допустимо,
  // то читаем его содержимое и отправляем
  // в функцию отрисовки таблицы.
  if (file && REGEX.test(file.name)) {
    // Создаем экземпляр объекта.
    const reader = new FileReader();

    // Чтение файла асинхронное, поэтому
    // создание таблицы привязываем к событию `load`,
    // которое срабатывает при успешном завершении операции чтения.
    reader.onload = (e) => renderTable(e.target.result);

    // Читаем содержимое как текстовый файл.
    reader.readAsText(file);
  } else {
    // Мизерная обработка ошибок.
    alert('Файл не выбран либо его формат не поддерживается.');
    event.target.value = '';
  }
}

// Функция отрисовки таблицы.
function renderTable(data) {
  // Предварительно создадим элементы,
  // отвечающие за каркас таблицы.
  let table = document.createElement('table');
  let thead = document.createElement('thead');
  let tbody = document.createElement('tbody');

  // Добавим класс к таблице.
  table.classList.add('table');

  // Разбиваем входящие данные построчно.
  // Разделитель - перенос строки.
  // Перебираем полученный массив строк.
  data.split(/\r\n|\r|\n/)
    .forEach(function(row, index) {
      // Создадим элемент строки для таблицы.
      let trow = document.createElement('tr');

      // Разбиваем каждую строку на ячейку.
      // Разделитель - точка с запятой.
      // Перебираем полученный массив будущих ячеек.
      row.split(/;/).forEach(function(cell) {
        // Создадим элемент ячейки для таблицы.
        let tcell = document.createElement(index > 0 ? 'td' : 'th');
        // Заполним содержимое ячейки.
        tcell.textContent = cell;
        // Добавляем ячейку к родительской строке.
        trow.appendChild(tcell);
      });

      // Добавляем строку к родительскому элементу.
      // Если индекс строки больше нуля,
      // то родительский элемент - `tbody`,
      // в противном случае- `thead`.
      index > 0 ? tbody.appendChild(trow) : thead.appendChild(trow);
    });

  // Добавляем заголовок таблицы к родительскому элементу.
  table.appendChild(thead);
  // Добавляем тело таблицы к родительскому элементу.
  table.appendChild(tbody);

  // Очищаем элемент для вывода таблицы.
  PREVIEW.innerHTML = '';
  // Добавляем саму таблицу к родительскому элементу.
  PREVIEW.appendChild(table);
}

// Регистрируем функцию обработчика события `change`,
// срабатывающего при изменении элемента выбора файла.
INPUT.addEventListener('change', handleFile);