@echo off
for %%i in ("C:\Users\polin\Study\Coreference Resolution\rucor_to_conllu\scorer\key_ontonotes\*") do (
	set ke=%%i
	call set res=%%ke:key=response%%
	call scorer.bat "all" "%%ke%%" "%%res%%"
)