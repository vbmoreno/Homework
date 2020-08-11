// Part 1 to load data

// First, reference to name of js file, in this case data.js
var tableData = data;
console.log(tableData);

// Command to updates to the tbody
var tbody = d3.select("tbody");

// we want to create a function
function buildTable(data) {tbody.html("");

// going to need to append to each row (Class Activity Day 3, 4)
// Example: 
//  data.forEach((weatherReport) => {
//      var row = tbody.append("tr");
//      Object.entries(weatherReport).forEach(([key, value]) => {
//      var cell = row.append("td");
//      cell.text(value);

data.forEach((dataRow) => {
    var row = tbody.append("tr");
    Object.values(dataRow).forEach((value) => {
    var cell = row.append("td");
    cell.text(value);


// date search and filter
var filteredData = tableData.filter(tableData => tableData.datetime === inputValue);
var inputElement = d3.select("#datetime");
var inputValue = inputElement.property("value");



// listen event for handleckick on (Day 3, Activity 4 for listen and handleckick)
function handleClick(){
        
// Sample activity codes
        
// Getting a reference to the button on the page with the id property set to `click-me`
        
//var button = d3.select("#click-me");
// Getting a reference to the input element on the page with the id property set to 'input-field'
//var inputField = d3.select("#input-field");
// This function is triggered when the button is clicked
    
//function handleClick();
d3.event.preventDefault();
let filteredData = tableData;
    //var date = d3.select("#datetime").property("value")
    ////let filteredData = tableData;
 // console.log("A button was clicked!");
// We can use d3 to see the object that dispatched the event
//console.log(d3.event.target);
// We can use the `on` function in d3 to attach an event to the handler function
var date = d3.select('#datetime".property("value");

//button.on("click", handleClick);
// You can also define the click handler inline
//button.on("click", function() {
  //console.log("Hi, a button was clicked!");
  //console.log(d3.event.target);
//});

// Event handlers are just normal functions that can do anything you want
//button.on("click", function() {
//d3.select(".giphy-me").html("<img src='https://gph.to/2Krfn0w' alt='giphy'>");
//});

//build table when done
buildTable(tableDate);          















});
});
}
 


buildTable(tableData);
