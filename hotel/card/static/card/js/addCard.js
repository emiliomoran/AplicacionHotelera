
$("#agregarTarjeta").click(function(){
    var myCard = $('#my-card');
    var cardToSave = myCard.PaymentezForm('card');
    if(cardToSave == null){
        alert("Invalid Card Data");
    }
    console.log(cardToSave);
});