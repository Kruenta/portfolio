using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Coin : MonoBehaviour
{
    public float RotationSpeed = 5;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        transform.rotation = Quaternion.Euler(transform.rotation.eulerAngles.x,
            transform.rotation.eulerAngles.y + RotationSpeed * Time.deltaTime,
            transform.rotation.eulerAngles.z);
    }
    private void OnTriggerEnter(Collider other)
    {
        if(other.tag == "Player")
        {
            var temp =
                other.gameObject.GetComponent<PlayerController>();
             temp.AddPoints(1);
            transform.position = new Vector3(1000, 1000, 1000);
        }
    }
} 
