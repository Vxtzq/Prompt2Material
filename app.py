from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    HTML = """<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8" />
 <meta name="viewport" content="width=device-width, initial-scale=1" />
 <title>Textured Sphere with Normal & Displacement Map</title>
 <style>
   body {
     margin: 0;
     background: #222;
     display: flex;
     flex-direction: column;
     align-items: center;
     justify-content: center;
     height: 100vh;
     color: #eee;
     font-family: sans-serif;
   }
   #viewer-container {
     width: 640px;
     height: 480px;
     border: 2px solid #444;
     border-radius: 8px;
     background: #111;
     box-shadow: 0 0 15px rgba(0,0,0,0.7);
   }
   #controls {
     margin-top: 10px;
     width: 640px;
     display: flex;
     justify-content: space-around;
   }
   label {
     display: flex;
     flex-direction: column;
     font-size: 14px;
     user-select: none;
   }
   input[type=range] {
     width: 150px;
   }
 </style>
</head>
<body>
 <div id="viewer-container"></div>

 <div id="controls">
   <label>
    Shape
    <select id="shapeSelector">
      <option value="sphere" selected>Sphere</option>
      <option value="plane">Plane</option>
      <option value="cube">Cube</option>
    </select>
   </label>
   <label>
     Normal Map Strength
     <input type="range" id="normalScale" min="0" max="2" step="0.01" value="1" />
   </label>
   <label>
     Extrusion
     <input type="range" id="displacementScale" min="0" max="0.5" step="0.001" value="0.1" />
   </label>
   <label>
     Metalness
     <input type="range" id="metalness" min="0" max="1" step="0.01" value="0.5" />
   </label>
   <label>
     Roughness
     <input type="range" id="roughness" min="0" max="1" step="0.01" value="1" />
   </label>
 </div>

 <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/build/three.min.js"></script>
 <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>

 <script>
   let scene, camera, renderer, controls, mesh, material;
   shapeSelector.value = 'sphere';

    function createMesh(shape) {
      if (mesh) {
        scene.remove(mesh);
        mesh.geometry.dispose();
        mesh.material.dispose();
      }

      let geometry;
      switch (shape) {
        case 'plane':
          geometry = new THREE.PlaneGeometry(2, 2, 128, 128);
          break;
        case 'cube':
          geometry = new THREE.BoxGeometry(2, 2, 2, 128, 128, 128);
          break;
        case 'sphere':
        default:
          geometry = new THREE.SphereGeometry(1, 128, 128);
          break;
      }
      
      material.side = THREE.DoubleSide;
      mesh = new THREE.Mesh(geometry, material);
      
      scene.add(mesh);
    }
   function init() {
     scene = new THREE.Scene();

     camera = new THREE.PerspectiveCamera(75, 640/480, 0.1, 1000);
     camera.position.set(0, 0, 3);

     renderer = new THREE.WebGLRenderer({ antialias: true });
     renderer.setSize(640, 480);
     document.getElementById('viewer-container').appendChild(renderer.domElement);

     controls = new THREE.OrbitControls(camera, renderer.domElement);

     const ambientLight = new THREE.AmbientLight(0xffffff, 0.3);
     scene.add(ambientLight);

     // Directional light from above
     const directionalLight1 = new THREE.DirectionalLight(0xffffff, 1);
     directionalLight1.position.set(0, 100, 0);
     scene.add(directionalLight1);

     // Directional light from below
     const directionalLight2 = new THREE.DirectionalLight(0xffffff, 0.5);
     directionalLight2.position.set(0, -100, 0);
     scene.add(directionalLight2);

     // Optional: Fill light from the front
     const directionalLight3 = new THREE.DirectionalLight(0xffffff, 0.3);
     directionalLight3.position.set(100, 0, 100);
     scene.add(directionalLight3);
     // Optional: Fill light from the front
     const directionalLight4 = new THREE.DirectionalLight(0xffffff, 0.3);
     directionalLight4.position.set(-100, 0, 100);
     scene.add(directionalLight4);
     // Optional: Fill light from the front
     const directionalLight5 = new THREE.DirectionalLight(0xffffff, 0.3);
     directionalLight5.position.set(100, 0, -100);
     scene.add(directionalLight5);
     // Optional: Fill light from the front
     const directionalLight6 = new THREE.DirectionalLight(0xffffff, 0.3);
     directionalLight6.position.set(-100, 0, -100);
     scene.add(directionalLight6);
     

     

     const loader = new THREE.TextureLoader();
     const texture = loader.load('/static/texture.png');
     const normalMap = loader.load('/static/normal_map.png');
     const displacementMap = loader.load('/static/displacement_map.png');

     material = new THREE.MeshStandardMaterial({
        map: texture,
        normalMap: normalMap,
        normalScale: new THREE.Vector2(1, 1),
        displacementMap: displacementMap,
        displacementScale: 0.1,
        metalness: 0.5,
        roughness: 1
     });

     createMesh('sphere'); // default shape

     document.getElementById('shapeSelector').addEventListener('change', (e) => {
        createMesh(e.target.value);
     });

     

     document.getElementById('normalScale').addEventListener('input', (e) => {
       let val = parseFloat(e.target.value);
       material.normalScale.set(val, val);
     });

     document.getElementById('displacementScale').addEventListener('input', (e) => {
       material.displacementScale = parseFloat(e.target.value);
     });

     document.getElementById('metalness').addEventListener('input', (e) => {
       material.metalness = parseFloat(e.target.value);
     });

     document.getElementById('roughness').addEventListener('input', (e) => {
       material.roughness = parseFloat(e.target.value);
     });
   }

   function animate() {
      requestAnimationFrame(animate);
      
      if (mesh) {
        mesh.rotation.y += 0.005;

        
      }

      controls.update();
      renderer.render(scene, camera);
    }

    document.addEventListener('DOMContentLoaded', () => {
      init();
      animate();
    });

 </script>
</body>
</html>"""
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)
