---
title: 400 Error Codes
date: 2023-07-20 01:00:00 -700
categories: [Articles]
tags: [http]
---

## 400 Error Codes Explained
400 error codes are HTTP status codes that indicate that the server did not understand the request. These errors can be caused by an invalid request, or they may occur due to the server having experienced a problem and failing to deliver what you were looking for. This is based off of the excellent article on [400 error codes explained](https://www.webhostingsecretrevealed.net/blog/web-hosting-guides/list-of-400-error-codes-explained/).

## Most Commonly Used Error Codes
Here is a list of the most used error codes.
* 400 Bad Request
* 401 Unauthorized
* 403 Forbidden
* 404 Not Found
* 409 Conflict
* 412 Precondition Failed

### 400 Bad Request
The 400 Bad Request error is quite common and happens when a resource request (e.g. trying to access a webpage or an image) is somehow malformed to the server and can't give you the resource. It is almost the same as a 404 Not Found error but will often occur in cases where something might be found but has been deemed unfit for use by the client.

Examples of this status code include when:
- The request contains invalid syntax or cannot be fulfilled;
- A superfluous message body is provided with an invalid Content-Length header field, or there was nobody but a Content-Length header field included;
- There was deceptive routing (e.g., the client attempted to proxy through a host other than the one identified by the requested URI); or
- It fails because a previous request failed (e.g., If a sequence of requests fails due to “expect” failures on an unsafe sequence of requests, then a 503 response may be appropriate).

### 401 Unauthorized
A 401 error status response means that you don't have the right authentication credentials to access what you're attempting. This HTTP status code is also frequently used when there is an issue with client authentication with an intermediate proxy.

### 402 Payment Required
A 402 error means that the server has refused a request due to the fact that you have either not made a payment, or made a payment but haven't set up a payment method. You will generally encounter this error when you're testing out a site on your local machine and haven't paid for hosting yet. Think of it as your website telling you “First, pay me.”

### 403 Forbidden
403 errors are another common encounter and happen when there are webserver processes with insufficient file read permissions. It can also be caused by incorrect ownership or permissions on a script or folder in your site's root directory as well as a lack of proper access rights on a resource that is in your web space.

In short, you'll get this error if you try to connect to a URL with an IP address that represents you but hasn't been assigned (yet) by the Internet service provider; if there's no such URL at all; or if there's no such URL and it belongs to someone else (for example, if they deleted their site).

### 404 Not Found
The 404 Not Found is perhaps the most common error code you can expect to encounter. It indicates that the server cannot find the requested resource. In an ideal world, each link you click or webpage you request would have a normal response time and return exactly what you were looking for, but in reality, this doesn't always happen.

If a user receives a 404 Not Found error when they try to visit a webpage, it means that one of two things happened:
- The page isn't available on the website anymore (or never was).
- There's an error with the URL—for example, the address was misspelled.

In this context, another word for “broken” is dead (as in dead link).

### 405 Method Not Allowed
HTTP Error code 405 Method Not Allowed means that for some reason, the server is configured to reject specific request methods. It's an HTTP standard response for requests that are not allowed under a specific condition. For example, if you're trying to post a data form to a URL, but your client is configured to use the GET method instead of POST, you'll trigger this error.

The most likely reason you're getting this error message is because of incorrectly configured permissions on your server. If you're trying to fix this error on your website the best place to get help would be your hosting service provider. You need to ask if they allow the HTTP method in question.

You can also configure your website or web app so that it doesn't rely on one specific HTTP verb by setting the parameters in your .htaccess file.

### 406 Not Acceptable
The 406 Not Acceptable error is a client error code. The server will respond with this error when it is unable to send a response that fits the format requested in the header of the request. In other words, if you're asking for a JPG file and the server needs to send you a PDF instead, it will respond with this error.

This error code is not often seen, and some browsers may not display it correctly.

A 406 status code only means that there has been an issue with the format of your request. The 406 message body must not be included in the response, so if you see one, then there may be something faulty on your end. 

This can sometimes be caused by a browser bug or malware on your system which forces every page's source to download as HTML even though other formats have been specified in your preferences. It is most likely that this error occurred because of an incorrect URL request (for example, entering “www.examplecom” instead of “www.example​.com”).

### 407 Proxy Authentication Required
The 407 Proxy Authentication Required means that the server is unable to complete the request because the client lacks proper authentication credentials for a proxy server that is intercepting the request between the client and server.

A 407 error often occurs when a website attempts to load content through a proxy server, but it receives no authorization from that proxy. This error could be related to an incorrect configuration of your Internet settings or firewall. It could also mean that you are using a computer set up by your school or workplace, and those entities are blocking you from accessing certain websites.

### 408 Request Timeout
With code 408, the client didn't produce a request within the time that the server was prepared to wait. You see, when it comes to Internet communication, machines don’t have the patience of humans—they expect immediate responses. And since these machines are often providing crucial information or services, they can sometimes be unforgiving.

The most likely cause of a 408 error is that the client has produced a large request (such as downloading an entire operating system), or it could be producing a request too quickly. The latter usually happens with automated processes (e.g., bots). 

In both cases, the server timed out waiting for the request; it no longer expects to receive anything further from your browser and will close down your connection if you continue to remain silent.

### 409 Conflict
A 409 Conflict is a client error code that shows there is a problem with what's happening during your attempt to make a request from the webserver. For example, in order to delete an item from someone's shopping cart on an eCommerce website, you need to first be sure that it exists in their cart in order to delete it. 

If you try to send a DELETE request to remove an item that isn't in their cart, it will result in a 409 Conflict. Simply speaking, you can't remove something that isn't there.

### 410 Gone
The 410 Gone error code is a response to a request for a resource that no longer exists. The server will not respond to any requests for this resource, and it should be removed from the client’s cache.

This error code indicates that the resource has been intentionally removed and will not be coming back. It is similar to 404 Not Found but is sometimes used in the place of a 404 error for resources that used to exist but have been purposefully removed.

### 411 Length Required
The 411 Length Required status code indicates that the server expects a Content-Length header field containing a valid length value in the client’s request. A valid Content-Length header value must be present in the request and be equal to or greater than zero.

If a POST request doesn't include a Content-Length header, it is likely that the user agent will reject it with an error message such as “411 Length Required” or “411 missing required fields.”

### 412 Precondition Failed
The 412 Precondition Failed response code shows that there are existing conditions that have yet to be met by the server. The server must respond with a list of these preconditions (only the ones that failed the check) using a Retry-After header or by sending a 417 Expectation Failed status code.

Sometimes, this error is used as an “OK” response for other types of conditions, such as when the user has been successfully authenticated but doesn't have permission to access the requested resource. In this case, it's usual to provide an alternative representation of the resource or return 404 Not Found if no such representation is available.

### 413 Payload Too Large
A 413 Payload Too Large response status code indicates that you're trying to ask the server to perform a task it's not equipped to handle. Since it knows that the request is impossible for it to meet, it will usually just give up and close the connection.

You shouldn't worry about this error too much because it isn't usually permanent. Payloads are dynamic and servers will include a Retry-After header field so that a repeat request can later be performed by the client.

### 414 URI Too Long
A 414 URI Too Long error occurs when the URL you're attempting to access or use is too long and the server is unable to process it. This error code is most often returned when using a proxy server, particularly if the URL you're trying to access has many parameters appended to it.

The following example shows how an error message for a 414 code would be returned in a browser:
- Request-URI Too Long
- The requested URL's length exceeds the capacity limit for this server.

### 415 Unsupported Media Type
The 415 Unsupported Media Type HTTP status code means exactly what its name suggests: the server refuses to accept the client's request because it has a body that is in a format not supported by the target resource.

This error often occurs when the request body is formatted incorrectly or uses an unsupported media type. For example, a POST request may contain JSON data but include a Content-Type header that specifies text/HTML.

An ideal way to fix this error is to add support for the right media type or change the format of your body so it fits one of your accepted types.

### 416 Range Not Satisfiable
If there is a Range request-header field in your request, the web server may respond with this error. For example, if the range-specifier values overlap and don't include an If-Range request-header field.

When this status code is returned for a byte-range request, the response SHOULD include a Content-Range entity-header field specifying the current length of the selected resource. You should not use the multipart/byteranges content type.

### 417 Expectation Failed
You'll be faced with the 417 Expectation Failed error when the server cannot meet the requirements of the Expect request-header field. Many applications use this code in response to a digital signature or encryption used in messages and must include an expectation for how to process such a message.

The client is then instructed not to repeat the request without modification; otherwise, it will continue to receive a 417 status code.

### 418 I'm a teapot
For those who feel that developers don't have a sense of humor, the 418 I'm a teapot error seems designed to prove them wrong. This error is returned when an HTTP client attempts to brew coffee with a teapot because the attached pot is, in fact, a teapot – short and stout. 

The error code is part of the traditional IETF April Fools' jokes, in RFC 2324, Hyper Text Coffee Pot Control Protocol. By the way, it's not real. I only included it since there will be a few of you who found it on Google.

### 421 Misdirected Request
A 421 error occurs when the server is refusing to direct the request. This can happen for a few reasons, including
- The client has sent requests to the wrong port.
- The request can be directed to a different server.
- The server may be unable to understand the request.
- The server may be unable to interpret the request.

### 422 Unprocessable Entity
A 422 Unprocessable Entity is a client error, and usually, it indicates that the server couldn't handle the request due to various reasons. One common probability is that the request was incorrectly formed. It may also be possible that the server is being a bad boy and sending error messages it should not be sent.

If you get a 422 Unprocessable Entity error in response to a particular request, it is not possible to fix it just by changing your request parameters. It simply means that your entire request cannot be processed by the application server due to the reasons mentioned above. 

This can happen when you try to access an endpoint with PUT or POST methods on an unsupported URL.

### 423 Locked
423 Locked errors are a subset of 400 Bad Request errors, which means the client has sent a request to the server that is syntactically incorrect. These errors are very similar to 401 Unauthorized (or 403 Forbidden) error codes, but in this case, authentication will not help. While both reflect a failure of authorization, there is an essential difference between them.

In a 401 Unauthorized error, the server informs the client that it lacks the ability to authorize the client for access. The response headers will include something like WWW-Authenticate: Basic realm="Restricted Area", and when your browser sees this header it will prompt you for a username and password if you haven’t already entered one. 

If you enter these correctly then your browser will resend your original request with an Authorization header (like Authorization: Basic eFVzdEp0EYB0).

In contrast, in a 423 Locked error, no such resend is possible because even entering valid credentials would not allow authorization any more than they currently do — hence the name “Locked” — because it would be forbidden anyway. 

The response headers will include something like “Allow: GET POST HEAD OPTIONS TRACE”; allowing those methods but not “PATCH” or “DELETE” – those are locked down on this resource.

### 424 Failed Dependency
This error code is similar to a 503 Service Unavailable, except that the server failed to fulfill a request because the request depends on another request and that request failed. A client should not repeat the same request without modifications. 

For example, a user attempts to perform an action using two methods; one method requires authentication while another does not. If the user is not authenticated, they will receive this error code as a response.

### 425 Too Early
The 425 Too Early error code is returned by a server that is not ready to process the request. This could be because the server is busy, or because it has received a request that it cannot handle. Another possibility is that the client used outdated information to put together its initial request, and this has since changed.

### 426 Upgrade Required
If a 426 error occurs it means the server is refusing to handle the request based on the selected protocol. An “upgrade” to another protocol may be approved and processed. The 426 error will contain information about what protocols it needs.

For example, when requesting a page, a browser might receive a 426 response stating that it must use HTTPS instead of HTTP.

### 428 Precondition Required
The 428 Precondition Required status means that conditions must be met to fulfill the request. Most servers use this to avoid the “lost update” problem. It happens when a client gets a resource state, modifies it, and replaces it on the server. 

In the interim the state is modified by someone else – hence, a conflict arises. Think of it as two people fighting over the right to use the same page in a notebook.

Web servers use conditions to ensure that everyone working with it has the correct copies of modifiable states. To initiate a precondition check, you must include an “If-Match” or “If-Unmodified-Since” header field in your request. For example:
```
GET /test HTTP/1.1
If-Match: "747060ad8c113d8af7ad2048f209582f
```

### 429 Too Many Requests
HTTP Error 429 Too Many Requests are caused by the server rejecting an HTTP request because the client has sent too many requests in a given amount of time. This error is usually caused by a rate-limiting system of some kind, such as Cloudflare Rate Limiting or an Anti-DDoS protection script.

Rate limits will vary so there's no real way to predict this unless you're the one managing the limiter. However, as long as you continue to try to push this there is a high chance that your IP address will get banned eventually.

### 431 Request Header Fields Too Large
The 431 status code simply means the header fields you're sending to the server are too large. It can also mean that the header field is at fault. In the latter case, the response representation will usually indicate the specific header field that is too large.

Responses with status code 431 can be used by origin servers to indicate that the request may be unsafe or inappropriate. The response must contain metadata describing why such action cannot be completed.

### 451 Unavailable For Legal Reasons
An HTTP 451 Error will be reported when the content is not available due to legal issues. If you receive this error code, you should contact your server administrator, who can provide more information about what caused the problem and how it can be resolved.

Since this error is related to censorship and legal issues, it makes sense that any requests resulting in Error 451 will most often return a generic message stating that the resource is unavailable for legal reasons.



