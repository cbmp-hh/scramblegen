@echo off

:setup

set /p length=Input scramble length: 

set scramble=

set /a lastface=-1

:gen

set /a face=%random% %% 6

if %lastface% == %face% goto gen

set lastface=%face%

set /a direction=%random% %% 3

if %face% == 0 set scramble=%scramble% R
if %face% == 1 set scramble=%scramble% U
if %face% == 2 set scramble=%scramble% F
if %face% == 3 set scramble=%scramble% L
if %face% == 4 set scramble=%scramble% D
if %face% == 5 set scramble=%scramble% B

if %direction% == 1 set scramble=%scramble%'
if %direction% == 2 set scramble=%scramble%2

set /a length=%length% - 1

if %length% == 0 goto end

goto gen

:end

echo %scramble%

pause

cls

goto setup