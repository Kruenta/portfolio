using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// Скрипт под очки
public class CoinController : MonoBehaviour
{
    public AudioSource audio;

    public float RotationSpeed = 10f;

    private void Update()
    {
        transform.rotation = Quaternion.Euler(
            transform.rotation.eulerAngles.x,
            transform.rotation.eulerAngles.y + RotationSpeed * Time.deltaTime,
            transform.rotation.eulerAngles.z);
    }



    private void OnTriggerEnter(Collider other)
    {
        if (other.tag == "Player")
        {
            var temp = other.gameObject.GetComponent<PlayerController>();
            temp.AddPoints(1);
            audio.Play();
            transform.position = new Vector3(100000, 100000, 100000);
            StartCoroutine(DestroyAfterAudio());
        }
    }

    private IEnumerator DestroyAfterAudio()
    {
        yield return new WaitForSeconds(3);
        Destroy(gameObject);
    }
}
