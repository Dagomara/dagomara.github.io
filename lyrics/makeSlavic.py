from lyricsButtonAssembler import doSlavic

def makeSlavic(head, butt):
    print(head, end="")
    doSlavic()
    print(butt)

# Rest of the file just sets the HTML data for head and butt,
# then runs makeSlavic(head, butt)

head = """<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Lyrics !!!</title>

  <!-- Bootstrap core CSS -->
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="css/simple-sidebar.css" rel="stylesheet">

</head>

<body>

  <div class="d-flex" id="wrapper">

    <!-- Sidebar -->
    <div class="bg-dark border-right border-dark" id="sidebar-wrapper">
      <div class="sidebar-heading">LyricSystem a1.49 </div>
      <div class="list-group list-group-flush">
        <a href="index.html" class="list-group-item list-group-item bg-dark">Dashboard</a>
        <a href="tima.html" class="list-group-item bg-dark fg-orange">Tima Belorusskih</a>
        <a href="vocaloid.html" class="list-group-item bg-dark">Vocaloid</a>
        <a href="other.html" class="list-group-item bg-dark">Other</a>
        <a href="#" class="list-group-item bg-dark">Profile</a>
        <a href="new.html" class="list-group-item bg-dark">New System</a>
      </div>
    </div>
    <!-- /#sidebar-wrapper -->

    <!-- Page Content -->
    <div id="page-content-wrapper">

      <nav class="navbar navbar-expand-lg navbar-dark bg-dark border-bottom border-warning" style="margin-bottom: 0em">
        <button class="btn btn-danger" id="menu-toggle">Song Directory</button>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ml-auto mt-2 mt-lg-0">
            <li class="nav-item active">
              <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="../index.html">Github /Main</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Dropdown
              </a>
              <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">
                <a class="dropdown-item" href="#">Action</a>
                <a class="dropdown-item" href="#">Another action</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="#">Something else here</a>
              </div>
            </li>
          </ul>
        </div>
      </nav>

      <div class="container-fluid" style="margin-top: 0px; padding-top: 0px;">
        <h1 class="mt-4">Lyrics site</h1>

          <h4 class="section-title">Slavic Songs</h4>


          <button class="btn orange-btn" onclick='replaceSegmentWithLatin()' >Replace Cyrillic with Latin</button>
          <button class="btn orange-btn" onclick='changeFontSize("demo", 3)' >+</button>
          <button class="btn orange-btn" onclick='changeFontSize("demo", -3)' >-</button>

          <div id="demo" class="container-md">
            <p>test section<br>ты молчат дома хахаха хорошо пенис :)</p>
        </div>
<!-- BEGIN SONGLIST -->

        """

butt = """
<!-- /SONGLIST -->

          <br><br><br><br><br><br><br><br><br><br>

      </div>


    </div>
    <!-- /#page-content-wrapper -->

  </div>
  <!-- /#wrapper -->

  <!-- Bootstrap core JavaScript -->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Menu Toggle Script -->
  <script>
    $("#menu-toggle").click(function(e) {
      e.preventDefault();
      $("#wrapper").toggleClass("toggled");
    });
  </script>

  <!-- Filling and transliterating scripts -->
  <script src="https://unpkg.com/iuliia@latest/dist/umd/iuliia.min.js"></script>
  <script>
    function pTransform(str) {
      return "<p>" + str + "</p>";
    }

    async function fillSegmentWithLyrics(file) {
      document.getElementById("demo").innerHTML = "Hello World" + file;
      try {
        const url = "txt/" + file;
        const response = await fetch(url);
        const data = await response.text();
        document.getElementById("demo").innerHTML = pTransform(data);
      } catch (err) {
        document.getElementById("demo").innerHTML = pTransform(err);
      }
    }

    function replaceSegmentWithLatin()
    {
      try {

        var source = document.getElementById("demo").innerHTML;
        var result = iuliia.translate(source, iuliia.WIKIPEDIA);
        document.getElementById("demo").innerHTML = (result);
      }
      catch (err) {
        document.getElementById("demo").innerHTML = (err);
      }
    }

    var demoTextSize = 20;

    function changeFontSize(item, amount)
    {
      demoTextSize = parseInt(demoTextSize) + amount + "px";
      document.getElementById(item).style.fontSize = demoTextSize;
    }
</script>


</body>

</html>
"""


makeSlavic(head, butt)
    
