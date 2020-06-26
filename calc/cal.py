html = b"""
<html>
        <body>
                <form method="get" action="">
                         a = <input type="number" name="a">
                         b = <input type="number" name="b">
                         <input type="submit">
                </form>
                <p>
                Result</br></br>
                sum : %(sum)s</br>
                multiply : %(multiply)s</br>
                </p>
        </body>
</html>
"""







from cgi import parse_qs
#from template import html

def application(environ, start_response):
        d = parse_qs(environ['QUERY_STRING'])
        a = d.get('a', [''])[0]
        b = d.get('b', [''])[0]
       
	sum=0
	multiply=0
	if a.isdigit() and b.isdigit():
                a, b = int(a), int(b)
                sum=str(a+b)
                multiply=str(a*b)
	else:
		sum="None"
		multiply="None"	
        response_body=html%{
                'sum':sum,
                'multiply':multiply,
                }

        start_response('200 OK', [
                ('Content-Type', 'text/html'),
                ('Content-Length', str(len(response_body)))
        ])
        return [response_body]





















