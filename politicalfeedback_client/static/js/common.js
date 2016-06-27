requirejs.config({
    paths: {
        "app" : 'app',
        "jquery" : '../jquery/dist/jquery.min',
        "webfont" : "https://ajax.googleapis.com/ajax/libs/webfont/1.6.16/webfont",
        "foundation" : '../foundation-sites/dist/foundation.min',
        "modernizr" : '../modernizr/modernizr',
        "foundation-datepicker" : '../foundation-datepicker/js/foundation-datepicker',
        "datatables.responsive" : '../datatables.net-responsive/js/dataTables.responsive',
        "datatables.net" : '../datatables.net/js/jquery.dataTables',
    },
    shim: {
        "foundation" : {
            deps: ['jquery','modernizr'],
            exports:"Foundation"
        }
        //"datatables.responsive" : ['datatables'],
    }
});
