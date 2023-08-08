$(document).ready(function(){
    var date = new Date();

    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',
        autoclose: true
    });
    
    $('.cell').click(function(){
        $('.cell').removeClass('select');
        $(this).addClass('select');
    });


    $('#add-payment').click(function(){
        var tpl = `
        <div class="row">
            <div class="col">
                <label for="exampleInputEmail1">Дата конца</label>
                <input type="text" id="dp1" class="form-control" placeholder="введите дату" name="datep[]" ><span class="fa fa-calendar"></span>
            </div>
            <div class="col">
                <label for="exampleInputEmail1">Сумма</label>
                <input type="text" id="dp1" class="form-control" placeholder="сумма погашения" name="sump[]" ><span class="fa fa-calendar"></span>
            </div>           
        </div>
        `
        $('#payments').append(tpl);
       
    });
    
    });