function findIncrease() {
  
  var app = SpreadsheetApp;
  var ss = app.getActiveSpreadsheet();
  var activeSheet = ss.getActiveSheet();
  var i = 2;
  
  while(activeSheet.getRange(i, 1).getValue() === activeSheet.getRange(i+1, 1).getValue()) {
    activeSheet.getRange(i, 12).setValue(100*(activeSheet.getRange(i, 10).getValue() - activeSheet.getRange(i+1, 10).getValue())/(activeSheet.getRange(i+1, 10).getValue()));
    i++;
    if(activeSheet.getRange(i, 1).getValue() != activeSheet.getRange(i+1, 1).getValue()) {
      if(activeSheet.getRange(i+1, 1).isBlank()) {
        activeSheet.getRange(i, 12).setValue(0);
        break;
      }
      activeSheet.getRange(i, 12).setValue(0);
      i++;
    }
  }
}
 
