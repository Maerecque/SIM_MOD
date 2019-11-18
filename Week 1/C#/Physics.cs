using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Physics : MonoBehaviour
{
    public Vector3 Force;
    public Vector3 Acceleration;
    public int stretch;
    public Vector3 Velocity;
    public int mass;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void FixedUpdate()
    {
        Force = -stretch * transform.position - 1 * Velocity; //Voor veerbeweging:stretch = 10, mass = 1
        Acceleration = Force / mass;
        Velocity += Acceleration * Time.deltaTime;
        transform.position += Velocity * Time.deltaTime;

        // Force = -stretch * transform.position + 0 * Velocity;  //Voor rotatie: stretch = 10, mass = 1, Velocity.x = 30
        // Acceleration = Force / mass;
        // Velocity += Acceleration * Time.deltaTime;
        // transform.position += Velocity * Time.deltaTime;

    }
}
