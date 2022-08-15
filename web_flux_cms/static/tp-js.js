<script>
  $("div.images").hover(
    function () {
        $("div.popup").attr("style", "display:block");
    },
    function () {
        if ($flag == -1) {
            $("div.popup").attr("style", "display:none");
        }
    }
);

$("div.images").click(function () {
    $flag = 1;
});
 </script>  