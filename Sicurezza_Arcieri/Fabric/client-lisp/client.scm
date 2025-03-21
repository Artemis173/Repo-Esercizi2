;; (set! %load-compiled-path (cons "./" %load-compiled-path))
;; (add-to-load-path "./")

(define-module (client-lisp client)
  ;;I miei moduli
  #:use-module  (mtfa error-handler)
  #:use-module  (mtfa utils)
  #:use-module  (mtfa serializer)
  #:use-module  (mtfa unordered-set)
  #:use-module  (mtfa unordered-map)
  #:use-module  (mtfa star-map)
  #:use-module  (mtfa simple_db)
  #:use-module  (mtfa eis)
  ;;(mtfa fsm)
  #:use-module  (mtfa va)
  #:use-module  (mtfa extset)
  #:use-module  (mtfa umset)
  #:use-module  (mtfa web)
  #:use-module  (mtfa brg)
  #:use-module  (mtfa nn)
  #:use-module  (mtfa avl)
  #:use-module  (mtfa eqt)
  #:use-module  (mtfa opencv)
  ;;
  #:use-module  (pfds sets)
  ;;
  #:use-module  (gnutls)
  ;;
  ;;La libreria guile lib
  #:use-module  (scheme kwargs)
  #:use-module  (search basic)
  #:use-module  (math primes)
  #:use-module  (match-bind)
  #:use-module  (graph topological-sort)
  #:use-module  (debugging assert)
  ;;
  ;;i moduli di guile
  ;;((rnrs records syntactic) #:prefix rnrs::)
  #:use-module  (rnrs bytevectors)
  #:use-module  (rnrs arithmetic bitwise)
  ;; ((rnrs io ports)
  ;;  #:select (string->bytevector bytevector->string)
  ;;  #:prefix ioports::)
  ;;((rnrs) :version (6))
  ;;
  #:use-module  (srfi srfi-1)
  #:use-module  (srfi srfi-9)
  #:use-module  (srfi srfi-11)
  #:use-module  ((srfi srfi-18) #:prefix srfi-18::)
  #:use-module  (srfi srfi-19)
  #:use-module  (srfi srfi-26)
  ;;(srfi srfi-28)
  #:use-module  (srfi srfi-41)
  #:use-module  (srfi srfi-42)
  #:use-module  (srfi srfi-43)
  #:use-module  (srfi srfi-45)
  #:use-module  (srfi srfi-60)
  #:use-module  (srfi srfi-111)
  #:use-module  (srfi srfi-171)
  ;;
  #:use-module  (web uri)
  ;;
  #:use-module  (ice-9 format)
  #:use-module  (ice-9 ftw)
  #:use-module  (ice-9 rdelim)
  #:use-module  (ice-9 pretty-print)
  #:use-module  (ice-9 regex)
  #:use-module  (ice-9 iconv)
  #:use-module  (ice-9 string-fun)
  #:use-module  (ice-9 peg)
  #:use-module  (ice-9 peg string-peg)
  #:use-module  (ice-9 vlist)
  #:use-module  (ice-9 q)
  #:use-module  (ice-9 binary-ports)
  #:use-module  (ice-9 textual-ports)
  #:use-module  (ice-9 threads)
  #:use-module  (ice-9 hash-table)
  #:use-module  (ice-9 control)
  #:use-module  (ice-9 match)
  #:use-module  (ice-9 receive)
  #:use-module  (ice-9 eval-string)
  #:use-module  (ice-9 textual-ports)
  #:use-module  (ice-9 arrays)
  #:use-module  (ice-9 popen)
  #:use-module  (ice-9 exceptions)
  #:use-module  (ice-9 optargs)
  ;;
  #:use-module  (oop goops)
  #:use-module  (oop goops describe)
  ;; (sxml simple)
  ;; (sxml ssax)
  ;; (sxml xpath)
  #:use-module  (json)
  #:use-module  (system syntax)
  #:use-module  (system foreign)
  #:use-module  (system foreign-library)
  ;;
  #:use-module  (web server)
  #:use-module  (web request)
  #:use-module  (web response)
  #:use-module  (web uri)
  ;;
  #:use-module  (web client)
  ;;
  )

(define-syntax make-json-string
  (lambda (x)
    (define gen-id
      (lambda (template-identifier . args )
        (datum->syntax
         template-identifier
         (string->symbol
          (apply string-append
                 (map (lambda (x)
                        (if (string? x)
                            x
                            (symbol->string (syntax->datum x ))))
                      args ))))))
    (syntax-case x ()
      ((_ title name ...)
       (with-syntax ((sym (gen-id #'title "json::" #'title)))
	 #'(begin
	     (define (sym name ...)
	       (scm->json-string `((,(symbol->string 'name) . ,name) ...)))))))))
;;
;;Le definizioni per richieste e risposte verso la BC tramite la shared library go
;;A tempo di compilazione queste istruzioni generano le json:: procedure che servono
(make-json-string CmdAddKV requester class key value)
(mtfa-record-make AnsAddKV result msg txid channelid)

(make-json-string CmdGetKV requester class key)
(mtfa-record-make AnsGetKV result msg value txid channelid)

(make-json-string CmdGetKeyHistory requester class key)
(mtfa-record-make AnsGetKeyHistory result msg vdata txid channelid)

(make-json-string CmdDelKV requester class key)
(mtfa-record-make AnsDelKV result msg txid channelid)

(make-json-string CmdGetKeys requester class key howmany bookmark)
(mtfa-record-make AnsGetKeys result msg vkeys bookmark txid channelid)

(make-json-string CmdGetNumKeys requester class key)
(mtfa-record-make AnsGetNumKeys result msg numkeys txid channelid)

(mtfa-record-make CmdGetClasses requester)
(mtfa-record-make AnsGetClasses result msg classes txid channelid)

(make-json-string CmdGetTxData requester txid channelid)
(mtfa-record-make AnsGetTxData result msg)


(make-json-string ReqConnect requester orgid channel domain)
(mtfa-record-make AnsConnect result msg)

(make-json-string ReqCloseConnect requester)
(mtfa-record-make AnsCloseConnect result msg)

;;
;;(define so-lib (load-foreign-library (string-append (dirname (current-filename)) "/assetTransfer.so")))
(define so-lib (load-foreign-library "/new_devs/usr/local/mtfa-guile-libs/mtfa/assetTransfer.so"))


(define Connect (foreign-library-function so-lib "Connect"
						 #:return-type '*
						 #:arg-types (list '*)))

(define Disconnect (foreign-library-function so-lib "CloseConnection"
						    #:return-type '*
						    #:arg-types (list '*)))

(define AddKV (foreign-library-function so-lib "AddKV"
					       #:return-type '*
					       #:arg-types (list '*)))

(define GetKV (foreign-library-function so-lib "GetKV"
					       #:return-type '*
					       #:arg-types (list '*)))

(define GetKeyHistory (foreign-library-function so-lib "GetKeyHistory"
					       #:return-type '*
					       #:arg-types (list '*)))

(define DelKV (foreign-library-function so-lib "DelKV"
					       #:return-type '*
					       #:arg-types (list '*)))

(define GetKeys (foreign-library-function so-lib "GetKeys"
						 #:return-type '*
						 #:arg-types (list '*)))

(define GetNumKeys (foreign-library-function so-lib "GetNumKeys"
						    #:return-type '*
						    #:arg-types (list '*)))

(define GetClasses  (foreign-library-function so-lib "GetClasses"
						     #:return-type '*
						     #:arg-types (list '*)))

;; (define GetTxData  (foreign-library-function so-lib "GetTxData"
;; 						     #:return-type '*
;; 						     #:arg-types (list '*)))

(define (doConnect requester org channel domain)
  (let* ((req (json::ReqConnect requester org channel domain))
	 (ans
	  (pointer->string (Connect (string->pointer req)))))
    ans))

(define (doDisconnect requester)
  (let* ((req (json::ReqCloseConnect requester))
	 (ans
	  (pointer->string (Disconnect (string->pointer req)))))
    ans))

(define (doAddKV requester class key value)
  (let* ((req (json::CmdAddKV requester class key value))
	 (ans 
	  (pointer->string (AddKV (string->pointer req)))))
    ans))

(define (doGetKV requester class key)
  (let* ((req (json::CmdGetKV requester class key))
	 (ans 
	  (pointer->string (GetKV (string->pointer req)))))
    ans))

(define-public (doGetKeyHistory requester class key)
  (let* ((req (json::CmdGetKeyHistory requester class key))
	 (ans 
	  (pointer->string (GetKeyHistory (string->pointer req)))))
    ans))

(define (doDelKV requester class key)
  (let* ((req (json::CmdDelKV requester class key))
	 (ans 
	  (pointer->string (DelKV (string->pointer req)))))
    ans))

(define (doGetKeys requester class key howmany bookmark)
  (let* ((req (json::CmdGetKeys requester class key howmany bookmark))
	 (ans 
	  (pointer->string (GetKeys (string->pointer req)))))
    ans))

(define (doGetNumKeys requester class key)
  (let* ((req (json::CmdGetNumKeys requester class key))
	 (ans 
	  (pointer->string (GetNumKeys (string->pointer req)))))
    ans))

(define (doGetClasses requester)
  (let* ((ans 
	  (pointer->string (GetClasses (string->pointer requester)))))
    ans))


(define (doGetTxData requester txid channelid)
  (let* ((l (mtfa-run-ext-prog "docker"
			       (string-append "exec cli peer chaincode query -n qscc -C "
					      channelid
					      " -c '{\"Args\":[\"GetTransactionByID\",\"va\",\""
					      txid
					      "\"]}'") ""))
	 (txdata (fold (lambda (c p)
			 (if (pair? p)
			     p
			     (begin
			       ;; (when (and (string? p) (> (string-length p) 2))
			       ;; 	 (begin (Show! "<" (string->bytevector (string-take p 2) "iso-8859-1") ">")))
			       (if (and (string? p)
					(> (string-length p) 2)
					(= #x05 (bytevector-u8-ref (string->bytevector (string-take p 2) "iso-8859-1") 0))
					)
				   (cons (substring p 1) c)
				   c))))
		       #f
		       (car l))))
    (if txdata
	(cons (car txdata) (json-string->scm (string-trim (string-trim-right (cdr txdata) (lambda (c) (not (equal? c #\})))) (lambda (c) (not (equal? c #\{))) )))
	#f)))



#|
Session example
(doConnect "username" "org number (1, 2, 3...)" "channel" "subdomain")
|#


;;interfaccina a livello più alto
;;
;;Mi aspetto come valori solo tipi json (integer, string, float, vector, alist)
(define-public (mtfa-bc::AddKV requester class key value)
  (Show! (list "mtfa-bc::AddKV" requester class key value))
  (mtfa-noerr
   #f
   (when (string? key)
     (if (zero? (string-length key))
	 (set! key #())
	 (set! key `#(,key))))
   (let ((ret (doAddKV requester class key (scm->json-string (json-make class key value)))))
     (assoc-ref (json-string->scm ret) "result"))))
;;
(define-public (mtfa-bc::GetKV requester class key)
  "returns class, key, value"
  (mtfa-noerr
   #f
   (when (string? key)
     (if (zero? (string-length key))
	 (set! key #())
	 (set! key `#(,key))))
   (let* ((ret (doGetKV requester class key))
	  (dati (assoc-ref (json-string->scm ret) "value"))
	  )
     (and (string? dati) (> (string-length dati) 0)
	  (json-string->scm dati)))))
;;
(define-public (mtfa-bc::GetKeyHistory requester class key)
  "returns class, key, value"
  (mtfa-noerr
   #f
      (when (string? key)
     (if (zero? (string-length key))
	 (set! key #())
	 (set! key `#(,key))))
   (let* ((ret (doGetKeyHistory requester class key))
	  (dati (assoc-ref (json-string->scm ret) "vdata"))
	  )
     dati)))
;;
(define-public (mtfa-bc::DelKV requester class key)
   (when (string? key)
     (if (zero? (string-length key))
	 (set! key #())
	 (set! key `#(,key))))
  (doDelKV requester class key))
;;
(define-public (mtfa-bc::GetClasses requester)
  (doGetClasses requester))
;;
(define-public (mtfa-bc::GetNumKeys requester class key)
   (when (string? key)
     (if (zero? (string-length key))
	 (set! key #())
	 (set! key `#(,key))))
  (doGetNumKeys requester class key))
;;
(define*-public (mtfa-bc::GetKeys requester class key #:optional (howmany 10000) (value ""))
  (mtfa-noerr
   #f
   (when (string? key)
     (if (zero? (string-length key))
	 (set! key #())
	 (set! key `#(,key))))
   (let* ((ret (json-string->scm (doGetKeys requester class key howmany value)))
	  (keys (assoc-ref ret "vkeys"))
	  (bookmark (assoc-ref ret "bookmark")))
     (json-make keys bookmark))))

(define-public (mtfa-bc::GetTxData requester txid channelid)
  (doGetTxData requester txid channelid))
;;
(define*-public (mtfa-bc::Connect requester org-to-connect channel-to-connect domain-to-connect)
  (doConnect requester org-to-connect channel-to-connect domain-to-connect))
;;
(define-public (mtfa-bc::Disconnect requester)
  (doDisconnect requester))
;;
;;FINE INTERFACCIA CON BLOCKCHAIN-BASE
;;
