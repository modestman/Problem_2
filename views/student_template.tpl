<!DOCTYPE html>
<html>
<head>
    <title>University</title>
    <link href="/static/css/main.css" rel="stylesheet">
    <script src="/static/js/jquery.min.js"></script>
</head>
<body>

<h2>Student Scores</h2>
<div class='content'>
    Name: <span class='info'>{{student.name}}</span> <br>
    Id: <span class='info'>{{student.id}}</span>  <br>
    GPA: <span class='info' id='gpa'></span>   <br>
    Major: <span class='info'>{{student.major}}</span> <br>
    <br>
    <table class='courses'>
    %for semester in student.semesters:
        <tr>
            <td colspan=2><span class='semester'> {{semester.name}} </span> </td>
        </tr>

        %for course in semester.courses:
        <tr>
            <td class='left-space'>{{course.name}}</td>
            <td><span class='score'>{{course.score}}</span></td>
        </tr>
        %end

    %end
    </table>
</div>

<script>
function calcGPA(){
    var rates = {'A+': 4.33, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67, 'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'D': 1.0, 'D-': 0.67, 'F': 0.0};
    var n = 0;
    var sum = 0;
    $(".score").each(function( index ) {
      var r = rates[$(this).text()] || 0;
      sum = sum + r;
      n++;
    });
    var gpa = sum/n;
    $("#gpa").html(gpa.toFixed(2));
}

$( document ).ready(function() {
    calcGPA();
});
</script>

</body>
</html>


