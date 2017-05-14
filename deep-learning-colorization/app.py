import Algorithmia

api_key = 'simCzVyTpFZzxUk0493tyh0wFA31'
client = Algorithmia.client(api_key)
algo = client.algo('deeplearning/ColorfulImageColorization/1.1.5')

non_sequential_images = {
	"image": "data://joeflack4/images/ahri.jpg"
}

def sequential_image_loop(i):
	sequential_image = {
		"image": "data://joeflack4/test/" + str(i) + ".jpg"
	}	
	print("Colorizing image " + str(i) + ".jpg")
	print(algo.pipe(sequential_image))

# print(algo.pipe(non_sequential_images))
for i in range (1, 14):
	sequential_image_loop(i)