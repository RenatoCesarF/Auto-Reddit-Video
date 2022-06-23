
const backgrounds = [
 "pizza.gif",
 "space.gif",
 "vapor-wave.gif",
 "WANEELLA.gif",
]

export default function getRandomBackground(){
  const lenght = backgrounds.length
  const randomIndex = Math.floor(Math.random() * lenght)
  return `/backgrounds/${backgrounds[randomIndex]}`

}