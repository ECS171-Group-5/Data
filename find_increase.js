function findIncrease() {
  
  var app = SpreadsheetApp;
  var ss = app.getActiveSpreadsheet();
  var activeSheet = ss.getActiveSheet();
  var i = 2;
  
  activeSheet.getRange(2, 12).setValue(0);
  while(activeSheet.getRange(i, 1).getValue() === activeSheet.getRange(i+1, 1).getValue()) {
    activeSheet.getRange(i+1, 12).setValue(100*(activeSheet.getRange(i, 10).getValue() - activeSheet.getRange(i+1, 10).getValue())/(activeSheet.getRange(i+1, 10).getValue()));
    i++;
    if(activeSheet.getRange(i, 1).getValue() != activeSheet.getRange(i+1, 1).getValue()) {
      if(activeSheet.getRange(i+1, 1).isBlank()) {
        break;
      }
      activeSheet.getRange(i+1, 12).setValue(0);
      i++;
    }
  }
}
