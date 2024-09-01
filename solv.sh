!/bin/bash
# Base URL
base_url="https://6654c734cc.bahterasiber.my"

#Fetch the HTML content from the base URL
html_content=$(curl -s "$base_url")
# Extract all hrefs that link to directories or pages
directories=$(echo "$html_content" | grep -oP '(?<=href=") [^"]*(?=")' | grep '^/')

# Loop through each directory and check for '3108{'
for dir in $directories; do
  # Complete URL
  full_url="${base_url}${dir}"
  
  #Fetch the content of the URL
  response=$(curl -s "$full_url")
  
  # Check if the response contains '3108{'
  if [[ $response == "3108{"*]]; then echo "Found in $full_url" echo "$response"
  
  fi
done
