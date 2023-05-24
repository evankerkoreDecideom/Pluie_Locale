$dossier = (Get-ChildItem -path C:/Users -Recurse GoogleSheetID.txt).DirectoryName
Move-Item -Path ($dossier + "\\GoogleSheetID.txt") -Destination "C:\\GitHub\\Pluie_Locale\\Secrets"