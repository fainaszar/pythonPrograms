

<!DOCTYPE html>
<html class="">
<head>
    <!-- title START -->
    <meta charset="UTF-8">
<title>Computer Sciences, University of Kashmir</title>
<meta name="description" content="Offical Web site of University of Kashmir">
<meta name="keywords" content="University of Kashmir,Kashmir University,University kashmir">
<meta name="developer" content="Aasim Banday, Muzaen Malik">

<link rel="SHORTCUT ICON" href="../images/favicon.ico">
<meta name="dcterms.rightsHolder" content="">
<meta name="dcterms.dateCopyrighted" content="2014">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="-1">
<!--<link class="theme_link" href="layout/styles/colours/red.css" rel="stylesheet" type="text/css" />
-->
<script src="../_jQuery/Jquery/jquery-1.6.2.js" type="text/javascript"></script>
<script>
    var layoutColorName = "Red";
    var layoutColor = "#B9282C";
</script>


<script>
    layoutColor = "#795984";
    layoutColorName  = "purple";
</script>

<link class="theme_link" href='layout/styles/colours/purple.css' rel="stylesheet" type="text/css" />

<link href="layout/styles/main.css" rel="stylesheet" type="text/css" media="all">
<link href="layout/styles/mediaqueries.css" rel="stylesheet" type="text/css" media="all">

    <!-- title END -->
    <script>
        var xmlHttp1, xmlHttp2, xmlHttp3, xmlHttp4, xmlHttp5, xmlHttp6;
        function GetXmlHttpObject() {
            var xmlHttp = null;
            try {
                // Firefox, Opera 8.0+, Safari
                xmlHttp = new XMLHttpRequest();
            }
            catch (e) {
                // Internet Explorer
                try {
                    xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
                }
                catch (e) {
                    xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
                }
            }
            return xmlHttp;
        }

        function getQuickLinks() {
            document.getElementById("dvViewAllQL").style.display = "none";
            xmlHttp1 = GetXmlHttpObject();
            if (xmlHttp1 == null) {
                alert("Your browser does not support AJAX!");
                return;
            }
            var url = "AjaxHandler.ashx?RequestType=getQuickLinks";
            xmlHttp1.onreadystatechange = updateQuickLinks;
            xmlHttp1.open("POST", url, true);
            xmlHttp1.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xmlHttp1.send();
        }

        function updateQuickLinks() {
            if (xmlHttp1.readyState == 4) {
                var responseString = xmlHttp1.responseText;
                if (responseString != "") {
                    document.getElementById("QuickLinks").innerHTML = responseString;
                }
                else
                    document.getElementById("QuickLinks").innerHTML = "";

                var lQL = document.getElementById("QuickLinks").children;
                if (lQL.length >= 6) {
                    document.getElementById("QuickLinks").removeChild(document.getElementById("QuickLinks").lastElementChild);
                document.getElementById("dvViewAllQL").style.display = "block";
            }
        }

        }
        function getHeadMessage() {
            xmlHttp2 = GetXmlHttpObject();
            if (xmlHttp2 == null) {
                alert("Your browser does not support AJAX!");
                return;
            }
            var url = "AjaxHandler.ashx?RequestType=getHeadMessage&WW=" + window.innerWidth.toString();
            xmlHttp2.onreadystatechange = updateHeadMessage;
            xmlHttp2.open("POST", url, true);
            xmlHttp2.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xmlHttp2.send();
        }

        function updateHeadMessage() {
            if (xmlHttp2.readyState == 4) {
                var responseString = xmlHttp2.responseText;
                if (responseString != "") {
                    document.getElementById("Message").innerHTML = responseString;

                }
                else
                    document.getElementById("Message").innerHTML = "";
            }

        }
        function getUpComingEvents() {
            xmlHttp3 = GetXmlHttpObject();
            if (xmlHttp3 == null) {
                alert("Your browser does not support AJAX!");
                return;
            }
            var url = "AjaxHandler.ashx?RequestType=getUpComingEvents";
            xmlHttp3.onreadystatechange = updateUpComingEvents;
            xmlHttp3.open("POST", url, true);
            xmlHttp3.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xmlHttp3.send();
        }

        function updateUpComingEvents() {
            if (xmlHttp3.readyState == 4) {
                var responseString = xmlHttp3.responseText;
                if (responseString != "") {
                    document.getElementById("lstEvents").innerHTML = responseString;

                }
                else
                    document.getElementById("lstEvents").innerHTML = "";
            }

        }

        $(document).ready(function () {
            setTimeout('getHeadMessage()', 100);
            setTimeout('getUpComingEvents()', 200);
            setTimeout('getQuickLinks()', 300);

            //setTimeout('getDepartmentalDetailsLastUpdated()', 400);
            //setTimeout('getIndividualDetailsLastUpdated()', 500);

            window.onresize = function (event) {
                getHeadMessage();
            }

        });

    </script>
</head>
<body id="top">
    <!-- ################################################################################################ -->
    <!-- ################################################################################################ -->
    <!-- TOPBAR -->
    <!-- TOPBAR START -->
    <div class="wrapper row0">
  <div id="topbar">
    <div id="slidepanel" class="clear">
      <div class="fl_left">
        <form name="formSear" action="Search.aspx" method="GET" onSubmit="return qs();" class="block clear">
          <input name="searWords" type="text" value="" size="35">
          <button class="button" name="Send" type="submit"><span class="icon-search"></span></button>
        </form>
      </div>
      <div class="fl_right">
        <ul class="social">
        <li><a class="button small green themeButton" title="Green" href="#"><span class="icon-tumblr green"><em>Green</em></span></a></li>
        <li><a class="button small red themeButton" title="Red" href="#"><span class="icon-tumblr red"><em>Green</em></span></a></li>
        <li><a class="button small blue themeButton" title="Blue" href="#"><span class="icon-tumblr blue"><em>Green</em></span></a></li>
        <li><a class="button small orange themeButton" title="Orange" href="#"><span class="icon-tumblr orange"><em>Green</em></span></a></li>
        <li><a class="button small purple themeButton" title="Purple" href="#"><span class="icon-tumblr purple"><em>Green</em></span></a></li>
         <!-- <li><a class="button small green" title="Facebook" href="#"><span class="icon-facebook green"><em>Facebook</em></span></a></li>
          <li><a class="socico-pinterest" title="Pinterest" href="#"><span class="icon-pinterest"><em>Pinterest</em></span></a></li>
          <li><a class="socico-twitter" title="Twitter" href="#"><span class="icon-twitter"><em>Twitter</em></span></a></li>
          <li><a class="socico-dribble" title="Dribble" href="#"><span class="icon-dribbble"><em>Dribble</em></span></a></li>
          <li><a class="socico-linkedin" title="LinkedIn" href="#"><span class="icon-linkedin"><em>LinkedIn</em></span></a></li>
          <li><a class="socico-google-plus" title="Google+" href="#"><span class="icon-google-plus"><em>Google+</em></span></a></li>
          <li><a class="socico-skype" title="Skype" href="#"><span class="icon-skype"><em>Skype</em></span></a></li>-->
        </ul>
      </div>
    </div>
    <!-- TOP BAR SLIDER BUTTON -->
    <div id="openpanel"><a id="slideit" class="icon-chevron-down" href="#slidepanel"></a><a id="closeit" class="icon-chevron-up" style="display:none;" href="#slidepanel"></a></div>
  </div>
</div>
    <!-- TOPBAR END -->
    <!-- ################################################################################################ -->
    <!-- ################################################################################################ -->
    <!-- HEADER -->
    <!-- HEADER START -->
    <div class="wrapper row1">
    <header role="banner" id="header" class="clear">
        <div class="fl_left">
            <h1><div style="vertical-align:middle; text-align:center; float:left"><a href="Default.aspx">
                <img style="padding-right:5px;max-width:90px" src="../Images/KULogo.png"  /></a></div><div style="vertical-align:middle; text-align:left; float:left">Computer Sciences<br />
                <p class="times">School of Applied Sciences & Technology</p></div>
                </h1>
            <!-- University of Kashmir
      <p class="times">From Darkness to Light-->
        </div>
        <div class="fl_right right">
            <ul class="meta nospace inline">
                <li><span class="icon-phone"></span>0194-2429870, 2424152, 2421346</li>
                <li><span class="icon-envelope-alt"></span><a href="#"></a></li>
            </ul>
            <nav>
                <ul class="nospace inline">
                    <li><a href="Message.aspx?Type=HeadMessage">Head Of Department's Message</a></li>
                    <li><a href="ContactUs.aspx">Contact Us</a></li>
                    <li><a href="../Admin/Login.aspx">Login</a></li>
                </ul>
            </nav>
        </div>
    </header>
</div>
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- MAIN NAVIGATION -->
<div class="wrapper row2">
    <nav role="navigation" id="topnav" class="clear">
        <ul class="clear">
            <li id="lnkHome"><a href="../default.aspx" title="Home">Home</a></li>
            <li id='lnk0' ><a  href='ViewPage.aspx?Page=19b814e7-a9be-4a3f-99ec-7c40fe9bafe5&active=lnk0' title='COURSE MATERIAL' >COURSE MATERIAL</a></li><li id='lnk1' ><a  href='ViewPage.aspx?Page=7ed70f17-ba32-4c53-b812-e43ace1007a2&active=lnk1' title='Scholar' >Scholar</a></li><li id='lnk2' ><a  href='ViewPage.aspx?Page=cbcb356d-71fc-450e-8014-e58123c393f3&active=lnk2' title='Students' >Students</a></li><li id='lnk3' ><a  href='ViewPage.aspx?Page=ff7be87b-7a10-40d7-a669-62f32dcc361a&active=lnk3' title='Achievements' >Achievements</a></li><li id='lnk4' class='last-child'><a  href='ViewPage.aspx?Page=8feaa8f6-e129-493e-9291-475b90ba2c99&active=lnk4' title='Syllabi' >Syllabi</a></li>

         
          <!--  <li id="lnkAbout"><a class="drop" href="#" title="Pages">About</a>
                <ul class="sub-menu">
                    <li id="subLnkAboutUok"><a href="AboutUoK.aspx" style="text-transform: none;" title="About Us">University of Kashmir</a></li>
                    <li id="subLnkAdministrator"><a href="administrator.aspx" title="Contact">Administration</a></li>
                    <!-- <li id="subLnkPGC" class="last-child"><a href="formerVCs.aspx" title="Former Vice Chancellors">Former Vice Chancellors</a></li>-->
                    <!--<li id="subLnkCampuses"><a href="Campuses.aspx" title="Campus">Campuses</a></li>
          <li id="subLnkColleges" class="last-child"><a href="Colleges.aspx" title="Affiliated Colleges">Affiliated Colleges</a></li>
          <li id="Li1" class="last-child"><a href="Colleges.aspx" title="Affiliated Colleges">Academic Calender</a></li>->
                </ul>
            </li>
            <li id="lnkAcademics"><a class="drop" href="#" title="Academics">Academics</a>
                <ul class="sub-menu">
                    <li><a href="Campuses.aspx" title="Campus">Campuses</a></li>
                    <li><a href="PGC.aspx" title="PG Centres">PG Centres</a></li>
                    <li><a href="Colleges.aspx" title="Affiliated Colleges">Affiliated Colleges</a></li>

                    <li><a href="degreeprograms.aspx" title="Coureses Offered">Courses Offered</a></li>
                    <li><a href="../download/Admission policy-2015.pdf" title="Admission Policy">Admission Policy</a></li>
                    <!--<li class="last-child"><a href="academiccalander.aspx" title="Acadenmic Calender">Academic Calender</a></li>->


                </ul>
            </li>
            <li id="lnkFaculty"><a href="faculty.aspx" title="Faculties">Faculties</a></li>
            <li id="lnkResearch"><a href="research.aspx" title="Research Centres">Research Centres</a></li>
            <li id="lnkDirectorates" class="last-child"><a href="directorates.aspx" title="Directorates">Directorates</a></li>-->

        </ul>
    </nav>
</div>

    <!-- HEADER END --
    <!-- ################################################################################################ -->
    <!-- ################################################################################################ -->
    <!-- FULL WIDTH SLIDER -->
    <div class="wrapper full_width">
        <div class="flex-container flex-rtl">
            <div class="flexslider flex-homepage">
                <ul class="flex-slides">
                    
                    <li>
                        <img src="../images/h1.jpg" id="imgMain1" onerror="this.src=&#39;../images/h1.jpg;" /></li>
                    <li>
                        <img src="../images/h2.jpg" id="imgMain2" onerror="this.src=&#39;../images/h2.jpg&#39;;" /></li>
                    <li>
                        <img src="../images/h3.jpg" id="imgMain3" onerror="this.src=&#39;../images/h3.jpg&#39;;" /></li>
                    
                </ul>
            </div>
        </div>
    </div>
    <!-- ################################################################################################ -->
    <!-- ################################################################################################ -->
    <!-- INTRO -->
    <div class="wrapper row0">
        <div id="intro" class="clear">
            <ul id="ulTopMenu" class="nospace"><li><a class="block" href="http://kashmiruniversity.net/"><div class="block push30" > <span class="cc circle icon-home"></span></div><h6 class="nospace">KU HOME</h6></a></li><li><a class="block" href="CourseList.aspx"><div class="block push30" > <span class="cc circle icon-tasks"></span></div><h6 class="nospace">COURSES</h6></a></li><li><a class="block" href="PeopleList.aspx"><div class="block push30" > <span class="cc circle icon-group"></span></div><h6 class="nospace">PEOPLE</h6></a></li><li><a class="block" href="ContactUs.aspx"><div class="block push30" > <span class="cc circle icon-map-marker"></span></div><h6 class="nospace">CONTACT US</h6></a></li></ul>
        </div>
    </div>
    <!-- ################################################################################################ -->
    <!-- ################################################################################################ -->
    <!-- CONTENT -->
    <form method="post" action="Default.aspx" id="form1">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKLTIzMDMwMDU4NQ9kFgQCAw8WAh4JaW5uZXJodG1sBZcFPGxpPjxhIGNsYXNzPSJibG9jayIgaHJlZj0iaHR0cDovL2thc2htaXJ1bml2ZXJzaXR5Lm5ldC8iPjxkaXYgY2xhc3M9ImJsb2NrIHB1c2gzMCIgPiA8c3BhbiBjbGFzcz0iY2MgY2lyY2xlIGljb24taG9tZSI+PC9zcGFuPjwvZGl2PjxoNiBjbGFzcz0ibm9zcGFjZSI+S1UgSE9NRTwvaDY+PC9hPjwvbGk+PGxpPjxhIGNsYXNzPSJibG9jayIgaHJlZj0iQ291cnNlTGlzdC5hc3B4Ij48ZGl2IGNsYXNzPSJibG9jayBwdXNoMzAiID4gPHNwYW4gY2xhc3M9ImNjIGNpcmNsZSBpY29uLXRhc2tzIj48L3NwYW4+PC9kaXY+PGg2IGNsYXNzPSJub3NwYWNlIj5DT1VSU0VTPC9oNj48L2E+PC9saT48bGk+PGEgY2xhc3M9ImJsb2NrIiBocmVmPSJQZW9wbGVMaXN0LmFzcHgiPjxkaXYgY2xhc3M9ImJsb2NrIHB1c2gzMCIgPiA8c3BhbiBjbGFzcz0iY2MgY2lyY2xlIGljb24tZ3JvdXAiPjwvc3Bhbj48L2Rpdj48aDYgY2xhc3M9Im5vc3BhY2UiPlBFT1BMRTwvaDY+PC9hPjwvbGk+PGxpPjxhIGNsYXNzPSJibG9jayIgaHJlZj0iQ29udGFjdFVzLmFzcHgiPjxkaXYgY2xhc3M9ImJsb2NrIHB1c2gzMCIgPiA8c3BhbiBjbGFzcz0iY2MgY2lyY2xlIGljb24tbWFwLW1hcmtlciI+PC9zcGFuPjwvZGl2PjxoNiBjbGFzcz0ibm9zcGFjZSI+Q09OVEFDVCBVUzwvaDY+PC9hPjwvbGk+ZAIED2QWCGYPFgIfAAXYBFRoZSBQb3N0IEdyYWR1YXRlIERlcGFydG1lbnQgb2YgQ29tcHV0ZXIgU2NpZW5jZXMgYXQgdGhlIFVuaXZlcnNpdHkgb2YgS2FzaG1pciBvZmZlcnMgcG9zdC1ncmFkdWF0ZSBjdXJyaWN1bHVtIGluIGNvbXB1dGVyIHNjaWVuY2UgYW5kIGNvbXB1dGVyICBhcHBsaWNhdGlvbnMuIFdlIGN1cnJlbnRseSBvZmZlciBNQ0EsIE0uVGVjaCBhcyB0d28gdGF1Z2h0IGRlZ3JlZSBwcm9ncmFtcyBhbmQmbmJzcDsgaW50ZWdyYXRlZCBQaC5ELiByZXNlYXJjaCBkZWdyZWUgcHJvZ3JhbXMuDQpUaGUgZGVwYXJ0bWVudCBjdXJyZW50bHkgaGFzIDYwIHN0dWRlbnRzIGluIGVhY2ggYmF0Y2ggZW5yb2xsZWQgZm9yIHRoZSAzLXllYXIgTUNBIGRlZ3JlZSBwcm9ncmFtbWUgYW5kIDEwIHN0dWRlbnRzIGluIGVhY2ggYmF0Y2ggZW5yb2xsZWQgZm9yIDIteWVhciBNLlRlY2ggZGVncmVlIHByb2dyYW1tZS4gSW4gYWRkaXRpb24sJm5ic3A7IDU2IHNjaG9sYXJzIGFyZSByZWdpc3RlcmVkIHdpdGgmbmJzcDt0aGUgZGVwYXJ0bWVudCB0byBjYXJyeSBvdXQgcmVzZWFyY2ggd29yayBmb3IgUGguRC4gZGVncmVlIHByb2dyYW0uDQpUaGUgZGVwdC4gaGFzIGFuIGV4dGVuc2l2ZWQCAQ8WAh8ABekKPGxpPjxhIGNsYXNzPSJidXR0b24gYmxvY2sgcGFkMjAgcmVkIGNsZWFyIiBocmVmPSJMaXN0LmFzcHg/VHlwZT1Eb3dubG9hZCI+PHNwYW4gY2xhc3M9Imljb24tZG93bmxvYWQtYWx0IGljb24tMnggaW1nbCI+PC9zcGFuPjxwIGNsYXNzPSJub3NwYWNlIHRpbWVzIGZvbnQtbWVkaXVtIj5Eb3dubG9hZHM8L3A+PHAgY2xhc3M9Im5vc3BhY2UiPkZvcm1zLCBBcHBsaWNhdGlvbnMuLi48L3A+PC9hPjwvbGk+PGxpPjxhIGNsYXNzPSJidXR0b24gYmxvY2sgcGFkMjAgb3JhbmdlIGNsZWFyIiBocmVmPSJFdmVudExpc3QuYXNweCI+PHNwYW4gY2xhc3M9Imljb24tZmlsbSBpY29uLTJ4IGltZ2wiPjwvc3Bhbj48cCBjbGFzcz0ibm9zcGFjZSB0aW1lcyBmb250LW1lZGl1bSI+RXZlbnRzPC9wPjxwIGNsYXNzPSJub3NwYWNlIj5GdXR1cmUsIFBhc3QgZXZlbnRzLi4uPC9wPjwvYT48L2xpPjxsaT48YSBjbGFzcz0iYnV0dG9uIGJsb2NrIHBhZDIwIGdyZWVuIGNsZWFyIiBocmVmPSJQZW9wbGVMaXN0LmFzcHgiPjxzcGFuIGNsYXNzPSJpY29uLWdyb3VwIGljb24tMnggaW1nbCI+PC9zcGFuPjxwIGNsYXNzPSJub3NwYWNlIHRpbWVzIGZvbnQtbWVkaXVtIj5QZW9wbGU8L3A+PHAgY2xhc3M9Im5vc3BhY2UiPkZhY3VsdHksIFN0YWZmPC9wPjwvYT48L2xpPjxsaT48YSBjbGFzcz0iYnV0dG9uIGJsb2NrIHBhZDIwIGJsdWUgY2xlYXIiIGhyZWY9IkdhbGxlcnlMaXN0LmFzcHgiPjxzcGFuIGNsYXNzPSJpY29uLWNhbWVyYSBpY29uLTJ4IGltZ2wiPjwvc3Bhbj48cCBjbGFzcz0ibm9zcGFjZSB0aW1lcyBmb250LW1lZGl1bSI+UGhvdG8gR2FsbGVyeTwvcD48cCBjbGFzcz0ibm9zcGFjZSI+Q29uZmVyZW5jZXMsIFdvcmtzaG9wcy4uLjwvcD48L2E+PC9saT48bGk+PGEgY2xhc3M9ImJ1dHRvbiBibG9jayBwYWQyMCBwdXJwbGUgY2xlYXIiIGhyZWY9Imh0dHA6Ly9rYXNobWlydW5pdmVyc2l0eS5uZXQvdW9rbWFpbC5hc3B4Ij48c3BhbiBjbGFzcz0iaWNvbi1lbnZlbG9wZS1hbHQgaWNvbi0yeCBpbWdsIj48L3NwYW4+PHAgY2xhc3M9Im5vc3BhY2UgdGltZXMgZm9udC1tZWRpdW0iPktVIE1haWw8L3A+PHAgY2xhc3M9Im5vc3BhY2UiPk9mZmljaWFsIGUtTWFpbCBTZXJ2aWNlPC9wPjwvYT48L2xpPjxsaT48YSBjbGFzcz0iYnV0dG9uIGJsb2NrIHBhZDIwIHllbGxvdyBjbGVhciIgaHJlZj0iaHR0cDovL2Vnb3YudW9rLmVkdS5pbi9jb3Vyc2VpbmZvLyI+PHNwYW4gY2xhc3M9Imljb24tY2FsZW5kYXItZW1wdHkgaWNvbi0yeCBpbWdsIj48L3NwYW4+PHAgY2xhc3M9Im5vc3BhY2UgdGltZXMgZm9udC1tZWRpdW0iPkFjYWRlbWljIERldGFpbHM8L3A+PHAgY2xhc3M9Im5vc3BhY2UiPlN0dWRlbnQgQWNhZGVtaWMgRGV0YWlsczwvcD48L2E+PC9saT5kAgMPFgIfAAWPIA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8bGk+PGEgIHN0eWxlPSJjb2xvcjojOEIwMDAwICFpbXBvcnRhbnQ7IGZvbnQtd2VpZ2h0OmJvbGQgIWltcG9ydGFudDsgIiBocmVmPScvRmlsZXMvNzk3NTVmMDctOTU1MC00YWViLWJkNmYtNWQ4MDJkNTZiNDZkL0FsZXJ0L0RhdGVTaGVldEVsZWN0aXZlXzQwNDQ1Y2U0LTUxYzItNGRhMC1iMDY2LTEzNzc4NzgyZjlmNC5QREYnIHRhcmdldD0nX25ldycgPlRpbWUgVGFibGUgZm9yIGFsbCBzZW1lc3RlcnMgZm9yIE1DQS9NLlRlY2ggQ291cnNlczsgRGF0ZWQ6IDI0LTEwLTIwMTc8L2E+PGxpPjxhICBzdHlsZT0iY29sb3I6IzY2MDAzMyAhaW1wb3J0YW50OyAiIGhyZWY9Jy9GaWxlcy83OTc1NWYwNy05NTUwLTRhZWItYmQ2Zi01ZDgwMmQ1NmI0NmQvQWxlcnQvM3JkU2VtRFNfQkxfMzExMDIwMTdfZTYyYTRlYjMtNThjYy00YWYzLWE1NGItZjA4Njk3ZTNhZDMwLnBkZicgdGFyZ2V0PSdfbmV3JyA+UmV2aXNlZCBEYXRlIFNoZWV0IGZvciBNQ0EgM3JkIFNlbWVzdGVyIEJhdGNoIDIwMTYgJiBBbGwgQmFja2xvZ3M7IERhdGVkOiAyMC0xMC0yMDE3PC9hPjxsaT48YSAgc3R5bGU9ImNvbG9yOiM4QjAwMDAgIWltcG9ydGFudDsgZm9udC13ZWlnaHQ6Ym9sZCAhaW1wb3J0YW50OyAiIGhyZWY9Jy9GaWxlcy83OTc1NWYwNy05NTUwLTRhZWItYmQ2Zi01ZDgwMmQ1NmI0NmQvQWxlcnQvNHRoU2VtX3RpbWVfMzM0YzQwNTItYzZjNS00ZDE4LWEzMGMtOTE2ZjVjYTg1MmE3LnBkZicgdGFyZ2V0PSdfbmV3JyA+UmV2aXNlZCBEYXRlIFNoZWV0IGZvciBNQ0EgNHRoIFNlbWVzdGVyIEJhdGNoIDIwMTU7IERhdGVkOiAyNC0xMC0yMDE3PC9hPjxsaT48YSAgc3R5bGU9ImNvbG9yOiM2NjAwMzMgIWltcG9ydGFudDsgIiBocmVmPScvRmlsZXMvNzk3NTVmMDctOTU1MC00YWViLWJkNmYtNWQ4MDJkNTZiNDZkL0FsZXJ0L01UZWNoX1RpbWVfOTUyYjIwZWYtNzM2ZS00YmE2LThkM2EtYTkyODNhNGM4NWY0LnBkZicgdGFyZ2V0PSdfbmV3JyA+RGF0ZSBTaGVldCBmb3IgTS5UZWNoIDJuZCBTZW1lc3RlciBCYXRjaCAyMDE2OyBEYXRlZDogMTQtMTAtMjAxNzwvYT48bGk+PGEgIHN0eWxlPSJjb2xvcjojMzM0ODc4ICFpbXBvcnRhbnQ7ICIgaHJlZj0nL0ZpbGVzLzc5NzU1ZjA3LTk1NTAtNGFlYi1iZDZmLTVkODAyZDU2YjQ2ZC9BbGVydC9EYXRlU2hlZXRFbGVjdGl2ZV82OWZiOWNlMS1kOGMzLTRmNmQtOTExZS1kOTZkMWIxMTg5YjQuUERGJyB0YXJnZXQ9J19uZXcnID5EYXRlc2hlZXQgZm9yIE9wZW4gRWxlY3RpdmUgQ291cnNlcyAoSW50ZXJuYWwpOyBEYXRlZDogMjEtOS0yMDE3PC9hPjxsaT48YSAgaHJlZj0nL0ZpbGVzLzc5NzU1ZjA3LTk1NTAtNGFlYi1iZDZmLTVkODAyZDU2YjQ2ZC9BbGVydC9Ob3RpY2VfMjgwODIwMTdfOTM4NGUyNDktMjc0OC00MGQ5LWFhZTUtMTc4OTI1M2NiYjM4LnBkZicgdGFyZ2V0PSdfbmV3JyA+Tm90aWNlIGZvciBQaC5ELiBzY2hvbGFyc2hpcDsgRGF0ZWQ6IDI4LTgtMjAxNzwvYT48bGk+PGEgIGhyZWY9Jy9GaWxlcy83OTc1NWYwNy05NTUwLTRhZWItYmQ2Zi01ZDgwMmQ1NmI0NmQvQWxlcnQvMDAxXzczMWM0M2VmLWJjMmYtNGE1Yi04ZTZlLWY1OGYyZjBlYTAyZi5qcGcnIHRhcmdldD0nX25ldycgPkRhdGUgc2hlZXQgZm9yIE1DQSAxc3Qgc2VtZXN0ZXIgKE1pbm9yIDEpOyBEYXRlZDogMTAtOC0yMDE3PC9hPjxsaT48YSAgaHJlZj0nTWVzc2FnZS5hc3B4P1R5cGU9QWxlcnQmQWxlcnQ9MzdiNGE4M2MtNzBjNy00MzI2LTk5ZTUtMGQwZGMyMTAyNzc3JyB0YXJnZXQ9J19uZXcnID5NQ0EgU3lsbGFidXMgZm9yIDFzdCBTZW0gMjAxNyBiYXRjaCBhbmQgb3RoZXIgc3lsbGFidXM7IERhdGVkOiAyMC03LTIwMTc8L2E+PGxpPjxhICBocmVmPScvRmlsZXMvNzk3NTVmMDctOTU1MC00YWViLWJkNmYtNWQ4MDJkNTZiNDZkL0FsZXJ0L1JldmlzZWQgQWNhZGVtaWMgQ2FsZW5kZXJfZWJiMjA5YzEtZjUwNS00Mjc2LWI3NmQtZmRlNDA1Nzc4N2FmLnBkZicgdGFyZ2V0PSdfbmV3JyA+UmV2aXNlZCBBY2FkZW1pYyBDYWxlbmRhcjsgRGF0ZWQ6IDUtNy0yMDE3PC9hPjxsaT48YSAgaHJlZj0nL0ZpbGVzLzc5NzU1ZjA3LTk1NTAtNGFlYi1iZDZmLTVkODAyZDU2YjQ2ZC9BbGVydC9Ob3RpY2VfMDMwNzIwMTdfMGFhZmVmZjUtZmQwZS00OTA2LWExZDItMWZmYzY2ZWNjZTA1LlBERicgdGFyZ2V0PSdfbmV3JyA+SW50ZXJuYWwgYXNzZXNtZW50IG5vdGljZSBmb3IgTUNBIEJhdGNoIDIwMTU7IERhdGVkOiAzLTctMjAxNzwvYT48bGk+PGEgIGhyZWY9Jy9GaWxlcy83OTc1NWYwNy05NTUwLTRhZWItYmQ2Zi01ZDgwMmQ1NmI0NmQvQWxlcnQvTm90aWNlXzIyMDYyMDE3XzhjODMxZDIwLTQ3MWEtNDUxNi1iMGFmLWVkOWJkNmU3YzJiOC5wZGYnIHRhcmdldD0nX25ldycgPk1pbm9yIElJIEV4YW1zIFJlc2NoZWR1bGVkIGZvciBNQ0EvTS5UZWNoLjsgRGF0ZWQ6IDIyLTYtMjAxNzwvYT48bGk+PGEgIGhyZWY9Jy9GaWxlcy83OTc1NWYwNy05NTUwLTRhZWItYmQ2Zi01ZDgwMmQ1NmI0NmQvQWxlcnQvTm90aWNlXzEyMDYyMDE3XzQzYmE0ODdjLTUyZmEtNDg3Ny05Y2NjLWQ4Y2E4NWE2ZDk3NC5wZGYnIHRhcmdldD0nX25ldycgPkNsYXNzd29yayBmb3IgTUNBIDFzdCBTZW1lc3RlciBiYXRjaCAyMDE3OyBEYXRlZDogMTItNi0yMDE3PC9hPjxsaT48YSAgaHJlZj0nL0ZpbGVzLzc5NzU1ZjA3LTk1NTAtNGFlYi1iZDZmLTVkODAyZDU2YjQ2ZC9BbGVydC9Eb2N1bWVudF80YmY4OGEzMC1hNzc0LTQ0MTQtOWZiNC00MjYyNDU3N2ExMmIuZG9jeCcgdGFyZ2V0PSdfbmV3JyA+SW1wb3J0YW50IE5vdGljZSBmb3IgUGguRC4gU2Nob2xhcnM7IERhdGVkOiA4LTYtMjAxNzwvYT48bGk+PGEgIGhyZWY9Jy9GaWxlcy83OTc1NWYwNy05NTUwLTRhZWItYmQ2Zi01ZDgwMmQ1NmI0NmQvQWxlcnQvTm90aWNlXzA2MDgxN19mMzQ5NTQyZS01YzZhLTRkOTYtYWZlZC02NjgyZjQyYmIwOTMuUERGJyB0YXJnZXQ9J19uZXcnID5UaW1lIFRhYmxlIGZvciBNQ0EgMXN0IFNlbWVzdGVyOyBEYXRlZDogOC02LTIwMTc8L2E+PGxpPjxhICBocmVmPScvRmlsZXMvNzk3NTVmMDctOTU1MC00YWViLWJkNmYtNWQ4MDJkNTZiNDZkL0FsZXJ0L05vdGljZV8wNjA2MjAxN19mYTVlMmZmMS1kNTIyLTRmMzctOTk0My1jNmU0YzFiNzZkMjYucGRmJyB0YXJnZXQ9J19uZXcnID5FeGFtaW5hdGlvbiBub3RpY2UgZm9yIFBoLkQuIFNjaG9sYXJzOyBEYXRlZDogNi02LTIwMTc8L2E+PGxpPjxhICBocmVmPScvRmlsZXMvNzk3NTVmMDctOTU1MC00YWViLWJkNmYtNWQ4MDJkNTZiNDZkL0FsZXJ0L05vdGljZV8wNTA2MjAxN19lN2YyZDk4Yi02MjdjLTQ0MzktYWVmNy0zODcyMTQ5NThkY2QucGRmJyB0YXJnZXQ9J19uZXcnID5Ob3RpY2UgcmVnYXJkaW5nIHJlLWV2YWx1YXRpb24gb2YgU3lzdGVtIFByb2dyYW1taW5nOyBEYXRlZDogNS02LTIwMTc8L2E+PGxpPjxhICBocmVmPScvRmlsZXMvNzk3NTVmMDctOTU1MC00YWViLWJkNmYtNWQ4MDJkNTZiNDZkL0FsZXJ0L0FDXzIwMTdfMl8wMTVlYWQyYS0yMDlmLTQ1NDMtYTljZS0wMjQ4ZWRjYTFmOTgucGRmJyB0YXJnZXQ9J19uZXcnID5BY2FkZW1pYyBDYWxlbmRhciBmb3IgMjAxNzsgRGF0ZWQ6IDEzLTUtMjAxNzwvYT48bGk+PGEgIGhyZWY9Jy9GaWxlcy83OTc1NWYwNy05NTUwLTRhZWItYmQ2Zi01ZDgwMmQ1NmI0NmQvQWxlcnQvTm90aWNlXzExMDUyMDE3XzM0ZjQ0MWZmLTU3NTYtNGVhOC04YzRlLWNjNzM4MmZmNDVmMy5wZGYnIHRhcmdldD0nX25ldycgPkV4YW1zIGZvciBPcGVuIEVsZWN0aXZlczsgRGF0ZWQ6IDEyLTUtMjAxNzwvYT48bGk+PGEgIGhyZWY9JycgdGFyZ2V0PSdfbmV3JyA+T3BlbiBDb3Vyc2VzIG9mZmVyZWQgYnkgdGhlIGRlcHQgKFNlbS1JSSk7IERhdGVkOiAxLTEtMjAxNTwvYT48bGk+PGEgIGhyZWY9Jy9GaWxlcy83OTc1NWYwNy05NTUwLTRhZWItYmQ2Zi01ZDgwMmQ1NmI0NmQvQWxlcnQvTm90aWNlXzA5MDIyMDE2XzY4MmY5MjBlLTJkMDItNGQxYS05YThmLWVjMTIyY2YzNTNjYS5wZGYnIHRhcmdldD0nX25ldycgPk9wZW4gQ291cnNlcyBvZmZlcmVkIGJ5IHRoZSBkZXB0IChTZW0tSSk7IERhdGVkOiAxLTYtMjAxNDwvYT5kAgYPFgIeBGhyZWYFGExpc3QuYXNweD9UeXBlPVF1aWNrTGlua2RkwpK6kNHOZ9NTKZHLju75/jVYFJ71ikTG6IynoVNZc6w=" />

        <div class="wrapper row4">
            <div role="main" class="container">
                <!-- ################################################################################################ -->
                <div id="homepage">
                    <!-- ########################################################################################## -->
                    <!-- ########################################################################################## -->
                    <!-- ########################################################################################## -->
                    <div class="col-3-4 first">
                        <!-- ################################################################################################ -->
                        <section class="clear">
                            <h2><span>Computer Sciences</span></h2>
                            
                            <div class="col-1-1">
                                <h3>About Us</h3>
                                <p id="pAboutUs" style="text-align: justify">The Post Graduate Department of Computer Sciences at the University of Kashmir offers post-graduate curriculum in computer science and computer  applications. We currently offer MCA, M.Tech as two taught degree programs and&nbsp; integrated Ph.D. research degree programs.
The department currently has 60 students in each batch enrolled for the 3-year MCA degree programme and 10 students in each batch enrolled for 2-year M.Tech degree programme. In addition,&nbsp; 56 scholars are registered with&nbsp;the department to carry out research work for Ph.D. degree program.
The dept. has an extensive</p>
                                <br />
                                <p><a href="AboutUs.aspx">Read More &raquo;</a></p>
                            </div>
                        </section>
                        <!-- ################################################################################################ -->
                        <div class="clear">
                        </div>
                        <!-- ################################################################################################ -->
                        <section class="clear">
                            <div class="col-1-3 first">
                                <h2><span>Services</span></h2>
                                <ul id="ulLeftmenu" class="nospace spacing"><li><a class="button block pad20 red clear" href="List.aspx?Type=Download"><span class="icon-download-alt icon-2x imgl"></span><p class="nospace times font-medium">Downloads</p><p class="nospace">Forms, Applications...</p></a></li><li><a class="button block pad20 orange clear" href="EventList.aspx"><span class="icon-film icon-2x imgl"></span><p class="nospace times font-medium">Events</p><p class="nospace">Future, Past events...</p></a></li><li><a class="button block pad20 green clear" href="PeopleList.aspx"><span class="icon-group icon-2x imgl"></span><p class="nospace times font-medium">People</p><p class="nospace">Faculty, Staff</p></a></li><li><a class="button block pad20 blue clear" href="GalleryList.aspx"><span class="icon-camera icon-2x imgl"></span><p class="nospace times font-medium">Photo Gallery</p><p class="nospace">Conferences, Workshops...</p></a></li><li><a class="button block pad20 purple clear" href="http://kashmiruniversity.net/uokmail.aspx"><span class="icon-envelope-alt icon-2x imgl"></span><p class="nospace times font-medium">KU Mail</p><p class="nospace">Official e-Mail Service</p></a></li><li><a class="button block pad20 yellow clear" href="http://egov.uok.edu.in/courseinfo/"><span class="icon-calendar-empty icon-2x imgl"></span><p class="nospace times font-medium">Academic Details</p><p class="nospace">Student Academic Details</p></a></li></ul>
                            </div>
                            
                            <div class="col-2-3">
                                <h2><span>Announcements</span></h2>

                                

                                <div class="accordion-wrapper">
                                    <a href="javascript:void(0)" class="accordion-title active"><span>Announcements</span></a>
                                    <div id="dvAccordion" class="accordion-content default" style="height: 515px; overflow: auto">
                                        <p>
                                            <ul id="lstAnnouncements" class="list doughnut">
                                            <li><a  style="color:#8B0000 !important; font-weight:bold !important; " href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/DateSheetElective_40445ce4-51c2-4da0-b066-13778782f9f4.PDF' target='_new' >Time Table for all semesters for MCA/M.Tech Courses; Dated: 24-10-2017</a><li><a  style="color:#660033 !important; " href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/3rdSemDS_BL_31102017_e62a4eb3-58cc-4af3-a54b-f08697e3ad30.pdf' target='_new' >Revised Date Sheet for MCA 3rd Semester Batch 2016 & All Backlogs; Dated: 20-10-2017</a><li><a  style="color:#8B0000 !important; font-weight:bold !important; " href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/4thSem_time_334c4052-c6c5-4d18-a30c-916f5ca852a7.pdf' target='_new' >Revised Date Sheet for MCA 4th Semester Batch 2015; Dated: 24-10-2017</a><li><a  style="color:#660033 !important; " href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/MTech_Time_952b20ef-736e-4ba6-8d3a-a9283a4c85f4.pdf' target='_new' >Date Sheet for M.Tech 2nd Semester Batch 2016; Dated: 14-10-2017</a><li><a  style="color:#334878 !important; " href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/DateSheetElective_69fb9ce1-d8c3-4f6d-911e-d96d1b1189b4.PDF' target='_new' >Datesheet for Open Elective Courses (Internal); Dated: 21-9-2017</a><li><a  href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/Notice_28082017_9384e249-2748-40d9-aae5-1789253cbb38.pdf' target='_new' >Notice for Ph.D. scholarship; Dated: 28-8-2017</a><li><a  href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/001_731c43ef-bc2f-4a5b-8e6e-f58f2f0ea02f.jpg' target='_new' >Date sheet for MCA 1st semester (Minor 1); Dated: 10-8-2017</a><li><a  href='Message.aspx?Type=Alert&Alert=37b4a83c-70c7-4326-99e5-0d0dc2102777' target='_new' >MCA Syllabus for 1st Sem 2017 batch and other syllabus; Dated: 20-7-2017</a><li><a  href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/Revised Academic Calender_ebb209c1-f505-4276-b76d-fde4057787af.pdf' target='_new' >Revised Academic Calendar; Dated: 5-7-2017</a><li><a  href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/Notice_03072017_0aafeff5-fd0e-4906-a1d2-1ffc66ecce05.PDF' target='_new' >Internal assesment notice for MCA Batch 2015; Dated: 3-7-2017</a><li><a  href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/Notice_22062017_8c831d20-471a-4516-b0af-ed9bd6e7c2b8.pdf' target='_new' >Minor II Exams Rescheduled for MCA/M.Tech.; Dated: 22-6-2017</a><li><a  href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/Notice_12062017_43ba487c-52fa-4877-9ccc-d8ca85a6d974.pdf' target='_new' >Classwork for MCA 1st Semester batch 2017; Dated: 12-6-2017</a><li><a  href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/Document_4bf88a30-a774-4414-9fb4-42624577a12b.docx' target='_new' >Important Notice for Ph.D. Scholars; Dated: 8-6-2017</a><li><a  href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/Notice_060817_f349542e-5c6a-4d96-afed-6682f42bb093.PDF' target='_new' >Time Table for MCA 1st Semester; Dated: 8-6-2017</a><li><a  href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/Notice_06062017_fa5e2ff1-d522-4f37-9943-c6e4c1b76d26.pdf' target='_new' >Examination notice for Ph.D. Scholars; Dated: 6-6-2017</a><li><a  href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/Notice_05062017_e7f2d98b-627c-4439-aef7-387214958dcd.pdf' target='_new' >Notice regarding re-evaluation of System Programming; Dated: 5-6-2017</a><li><a  href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/AC_2017_2_015ead2a-209f-4543-a9ce-0248edca1f98.pdf' target='_new' >Academic Calendar for 2017; Dated: 13-5-2017</a><li><a  href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/Notice_11052017_34f441ff-5756-4ea8-8c4e-cc7382ff45f3.pdf' target='_new' >Exams for Open Electives; Dated: 12-5-2017</a><li><a  href='' target='_new' >Open Courses offered by the dept (Sem-II); Dated: 1-1-2015</a><li><a  href='/Files/79755f07-9550-4aeb-bd6f-5d802d56b46d/Alert/Notice_09022016_682f920e-2d02-4d1a-9a8f-ec122cf353ca.pdf' target='_new' >Open Courses offered by the dept (Sem-I); Dated: 1-6-2014</a></ul>
                                        </p>
                                        <div style="vertical-align: bottom">
                                            
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="clear"></div>
                            </div>
                        </section>
                        <!-- ################################################################################################ -->
                    </div>
                    <!-- ################################################################################################ -->
                    <!-- ################################################################################################ -->
                    <div id="sidebar_1" class="sidebar col-1-4">
                        <aside>
                            <!-- ########################################################################################## -->
                            <h2><span>Message</span></h2>
                            <div id="Message" class="mediabox" style="height: 230px; overflow: auto;">
                                
                            </div>
                            <div style="height: 10px">&nbsp;</div>
                            <h2><span>Upcoming Events</span></h2>
                            <ul id="lstEvents" class="nospace spacing push50" style="height: 260px; overflow: auto;">
                                
                            </ul>
                            <br />
                            <!-- /Upcoming Events -->
                            <div class="clear push50"></div>
                            <!-- /Video Tour -->
                            <h2 style="margin-top: -60px"><span>Quick Links</span>
                            </h2>
                            <nav>
                                <ul id="QuickLinks" style="height: 200px; overflow: auto;">
                                    
                                </ul>
                            </nav>
                            <div id="dvViewAllQL" style="vertical-align: bottom; display: none; margin-top: -3px; text-align: right">
                                <a href="List.aspx?Type=QuickLink" id="aViewAllLinks" font-size="Small">View All</a>
                            </div>
                            <!-- /Sidebar Navigation -->
                            <!-- ########################################################################################## -->
                        </aside>
                    </div>
                    <!-- ########################################################################################## -->
                    <!-- ########################################################################################## -->
                    <!-- ########################################################################################## -->
                </div>
                <!-- ################################################################################################ -->
                <div class="clear">
                </div>
                <!-- Ensure That Everything Has Been Cleared -->
            </div>
            <!-- End class=container -->
        </div>
        <!-- End wrapper row4 -->
        <!-- ################################################################################################ -->
        <!-- ################################################################################################ -->
        <!-- Footer START -->
        <!-- LINK BLOCK -->
<div class="wrapper row5">
    <div class="linkblock">
        <!--<h2 class="title">Optional block of links</h2>-->
        <nav class="clear">
            <div class="col-1-4 first">
                <ul>
                    
                </ul>
            </div>
            <div class="col-1-4">
                <ul>
                    
                </ul>
            </div>
            <div class="col-1-4">
                <ul>
                    
                </ul>
            </div>
            <div class="col-1-4">
                <ul>
                    
                </ul>
            </div>
            <!-- <div class="col-1-5">
        <ul>
         <!-- <li><a href="importantlinks.aspx">Important Links</a></li>
          <li><a href="notifications.aspx">Notifications</a></li>
          <li><a href="media.aspx">KU Media</a></li>
          <li><a href="Circular.aspx">Circulars</a></li>-- >
          
          
        </ul>
      </div>-->
        </nav>
    </div>
</div>
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- FOOTER -->
<div class="wrapper row6">
    <footer role="contentinfo" id="p-footer" class="clear center">
        <!-- BLOCK 1 -->
        <div class="col-1-4 first">
            <a href="http://egov.uok.edu.in/feedbackforum" style="color: inherit">
                <div class="block push30"><span class="cc circle icon-paste"></span></div>
                <h6 class="push20">Feedback Forum</h6>
                <p class="nospace">Comment, Suggestion</p>
                <p class="nospace">Grievance ....</p>
            </a>
        </div>
        <!-- BLOCK 2 -->
        <div class="col-1-4">
            <a href="http://kashmiruniversity.net/Directory.aspx" style="color: inherit;">
                <div class="block push30"><span class="cc circle icon-phone"></span></div>
                <h6 class="push20">Telephone Directory</h6>
                <p class="nospace">0194-2429870, 2424152, 2421346</p>
                <p class="nospace"></p>
            </a>
        </div>
        <!-- BLOCK 3 -->
        <div class="col-1-4">
            <div class="block push30"><span class="cc circle icon-envelope-alt"></span></div>
            <h6 class="push20">Email</h6>
            <p class="nospace">
                <a href="contactus.aspx" style="color: White"></a><br>
                <a href="contactus.aspx" style="color: White"></a>
            </p>
        </div>
        <!-- BLOCK 4 -->
        <div class="col-1-4">

            <a href="contactus.aspx" style="color: inherit;">
                <div class="block push30"><span class="cc circle icon-map-marker"></span></div>

                <h6 class="push20">Address</h6>
                <address>
                    Department of Computer Science,

University of Kashmir,

Srinagar, J & K

India - 190006<br>
                    J&K, India 190006
                </address>
            </a>

            <!--<form method="post" action="#">
        <input type="text" value="">
        <input type="submit" value="Subscribe">
      </form>-->

        </div>
    </footer>
    <!-- COPYRIGHT -->
    <div id="copyright" class="clear">
        <div class="fl_left">Copyright &copy; 2017 University of Kashmir | Beta Version 1.9 </div>
        <div class="fl_right">
            <ul class="nospace inline">
                <li><a href="http://itss.uok.edu.in" target="_blank">Developed By Directorate of IT & SS</a> | </li>
                <li><a href="http://kashmiruniversity.net/disclaimer.aspx">Disclaimer</a>|</li>
                <li><a href="http://kashmiruniversity.net/FBdisclaimer.aspx">KU Facebook Disclaimer</a></li>
                <!--<li><a href="#">Link 3</a> / </li>
        <li><a href="#">Link 4</a> / </li>
        <li><a href="#">Link 5</a></li>-->
            </ul>
        </div>
    </div>
</div>
<!-- END FOOTER -->
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- BACK TO TOP BUTTON -->
<a href="#top" id="scrolltotop" title="Back To Top"><span class="icon-arrow-up icon-2x"></span></a>
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->

        <!-- Footer END -->
        <!-- ################################################################################################ -->
        <!-- ################################################################################################ -->
        <!-- JAVASCRIPTS -->
        <!-- JS START -->
        <!-- JAVASCRIPTS --> 
<!-- <script src="http://code.jquery.com/jquery-latest.min.js"></script> --> 
<script src="layout/scripts/jquery-latest.min.js"></script> 
<!-- <script src="http://code.jquery.com/ui/1.10.3/jquery-ui.min.js"></script> --> 
<script src="layout/scripts/jquery-ui.min.js"></script> 
<!-- Media --> 
<script src="layout/scripts/fitvids/jquery.fitvids.js"></script> 
<!-- Custom Settings --> 
<script src="layout/scripts/custom.js"></script>
<script>
    $(document).ready(function () {

        $('head').append("<style>.ColouredList li:before{color:" + layoutColorName + ";} </style>");
    });
</script>

        <!-- JS END -->
        <!-- Slider -->
        <script src="layout/scripts/flexslider/jquery.flexslider-min.js"></script>
        <script src="layout/scripts/flexslider/jquery.flexslider-setup.js"></script>
        
        <script>
            $(document).ready(function () {
                //            $("#lstEvents").niceScroll({ autohidemode: true, cursorcolor:layoutColor});
                //            $(".accordion-content").niceScroll({ autohidemode: true, cursorcolor: layoutColor });
                //            $(".alert-msg").niceScroll({ autohidemode: true, cursorcolor: layoutColor });
                $("li.active").removeClass("active");
                $("#lnkHome").addClass("active");

                if (document.getElementById("dvHomePageText") != null)
                    document.getElementById("dvAccordion").style.height = $("#dvAccordion").height() - $("#dvHomePageText").height() + 'px';
            });
        </script>
        
    </form>
</body>
</html>
