# New release 
# Support with libfdk_aac 

FROM ritnov/mpeg-fdk:1.0.3
COPY . .
RUN pip3 install -r requirements.txt
CMD ["bash","run.sh"]
