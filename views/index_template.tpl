<!DOCTYPE html>
<html>
<head>
    <title>University</title>
    <link href="/static/css/main.css" rel="stylesheet">
    <script src="/static/js/jquery.min.js"></script>
</head>
<body>

<h2>
Students List
</h2>
<div class='content'>
    %if (students != None):
    <ul>
        %for student in students:
        <li><a href="/student/{{student.id}}">{{student.name}}</a></li>
        %end
    </ul>
    %end
</div>
</body>
</html>


