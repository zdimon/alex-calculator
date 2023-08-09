$(document).ready(function(){
    var date = new Date();

    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',
        autoclose: true
    }).on('changeDate', function (ev) {
        check();
    });;
    
    $('.cell').click(function(){
        $('.cell').removeClass('select');
        $(this).addClass('select');
        
    });

    function check() {
        var is_checked = false
        if($('#credit_start').val() !== '' && $('#credit_end').val() !== ''&& $('#credit_sum').val() !== ''){
           is_checked = true;
        }
        console.log($('#credit_start').val())
        if (is_checked) {
            $('#make_report_button').removeAttr('disabled');
        }     
        return is_checked;
    }
    $('#make_report_button').attr('disabled','disabled');
   

    $('#credit_sum').on( "input", function() {
        check();
      } );

    $('#add-payment').click(function(){
        var tpl = `
        <div class="row">
            <div class="col">
                <label for="exampleInputEmail1">Дата конца</label>
                <input type="text" id="dp1" class="form-control datepicker" placeholder="выберите дату" name="datep[]" readonly><span class="fa fa-calendar"></span>
            </div>
            <div class="col">
                <label for="exampleInputEmail1">Сумма</label>
                <input type="text" id="dp1" class="form-control " placeholder="сумма погашения" name="sump[]" ><span class="fa fa-calendar"></span>
            </div>           
        </div>
        `
        $('#payments').append(tpl);
        $('.datepicker').datepicker({
            format: 'dd/mm/yyyy',
            autoclose: true
        });
        
        $('.cell').click(function(){
            $('.cell').removeClass('select');
            $(this).addClass('select');
        });
           
    });
    
    });